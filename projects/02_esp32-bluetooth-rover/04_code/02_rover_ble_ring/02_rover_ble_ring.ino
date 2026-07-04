#include <NimBLEDevice.h>
bool doConnect = false;
bool isConnected = false;
uint32_t scanTimeMs = 5000;

enum CarCommand : uint8_t { STOP, FORWARD, BACKWARD, LEFT, RIGHT };
CarCommand currentCommand = STOP;
CarCommand prevCommand = STOP;

static bool     clickActive = false;
static uint8_t  clickGroup  = 0;
static int16_t  firstX = 0, firstY = 0;
static int16_t  lastX  = 0, lastY  = 0;
static uint16_t activeCount = 0;

const char* targetAddrStr = "73:56:17:d7:39:ab";

static NimBLEAddress ringAddr;
static bool haveRingAddr = false;

static void startScanNow();
static void scanCompleteCB(NimBLEScanResults results);

static uint32_t lastScanKickMs = 0;
static volatile uint32_t lastOnResultMs = 0;

static void resetBluetoothStack() {
  Serial.println("RESET BLE STACK...");

  NimBLEScan* s = NimBLEDevice::getScan();
  if (s) {
    s->stop();
    s->clearResults();
  }

  NimBLEDevice::deinit(true);
  delay(80);

  NimBLEDevice::init("");
  NimBLEDevice::deleteAllBonds();

  lastScanKickMs = millis();
  lastOnResultMs = millis();

  startScanNow();
}

class ClientCallbacks : public NimBLEClientCallbacks {
  void onConnect(NimBLEClient* pClient) override {
    isConnected = true;
  }
  void onDisconnect(NimBLEClient* pClient, int reason) override {
    isConnected = false;
    startScanNow();
  }
} clientCallbacks;

class ScanCallbacks : public NimBLEScanCallbacks {
  void onResult(const NimBLEAdvertisedDevice* d) override {

    lastOnResultMs = millis();
    static uint32_t lastMarkMs = 0;
    uint32_t now = millis();
    if (now - lastMarkMs > 250) {
      Serial.println("***");
      lastMarkMs = now;
    }

    if (!d->isAdvertisingService(NimBLEUUID((uint16_t)0x1812))) return;

    std::string macStr = d->getAddress().toString();
    Serial.print("\n Found device MAC: ");
    Serial.println(macStr.c_str());

    if (strcasecmp(macStr.c_str(), targetAddrStr) != 0) return;

    Serial.println("Found MY device!");
    ringAddr = d->getAddress();
    haveRingAddr = true;

    NimBLEDevice::getScan()->stop();
    doConnect = true;
  }
} scanCallbacks;

static void startScanNow() {
  NimBLEScan* pScan = NimBLEDevice::getScan();
  pScan->stop();
  pScan->clearResults();
  delay(10);

  pScan->setScanCallbacks(&scanCallbacks, false);
  pScan->setInterval(100);
  pScan->setWindow(100);
  pScan->setActiveScan(false);
  Serial.println("Scan start");
  pScan->start(scanTimeMs, scanCompleteCB, false);
  lastScanKickMs = millis();
}

static void scanCompleteCB(NimBLEScanResults results) {
  if (!isConnected && !doConnect) {
    Serial.println("Scan ended -> restart");
    startScanNow();
  } else {
    Serial.println("Scan ended");
  }
}

static inline int16_t u16le_to_i16(uint8_t lo, uint8_t hi) {
  uint16_t u = (uint16_t)lo | ((uint16_t)hi << 8);
  return (int16_t)u;
}

void notifyCB(NimBLERemoteCharacteristic* pRemoteCharacteristic,
              uint8_t* pData, size_t length, bool isNotify) {
  if (length < 8) return;

  bool active  = (pData[6] != 0);
  bool release = (pData[6] == 0 && pData[7] == 0);

  if (active) {
    int16_t x = u16le_to_i16(pData[2], pData[3]);
    int16_t y = u16le_to_i16(pData[4], pData[5]);

    if (!clickActive) {
      clickActive = true;
      clickGroup = pData[1];
      firstX = lastX = x;
      firstY = lastY = y;
      activeCount = 1;
    } else {
      lastX = x;
      lastY = y;
      activeCount++;
    }
    return;
  }

  if (release) {
    if (!clickActive) return;

    if (clickGroup == 6 && activeCount == 1 && firstX == 1200 && firstY == 1012) {
      currentCommand = STOP;
    } else if (clickGroup == 7) {
      currentCommand = STOP;
    } else if (clickGroup == 4 || clickGroup == 5) {
      if (lastX < firstX) currentCommand = LEFT;
      else if (lastX > firstX) currentCommand = RIGHT;
      else currentCommand = STOP;
    } else if (clickGroup == 6) {
      if (lastY < firstY) currentCommand = FORWARD;
      else if (lastY > firstY) currentCommand = BACKWARD;
      else currentCommand = STOP;
    } else {
      currentCommand = STOP;
    }

    Serial.print("CLICK: ");
    Serial.println((int)currentCommand);

    clickActive = false;
    clickGroup = 0;
    activeCount = 0;
    return;
  }
}

void connectToServer() {
  Serial.println("Start connectToServer");
  doConnect = false;

  if (!haveRingAddr) {
    Serial.println("No ringAddr -> rescan");
    startScanNow();
    return;
  }

  NimBLEClient* pClient = NimBLEDevice::createClient();
  pClient->setClientCallbacks(&clientCallbacks, false);

  if (!pClient->connect(ringAddr)) {
    NimBLEDevice::deleteClient(pClient);
    Serial.println("Client is not ready");
    delay(100);
    resetBluetoothStack();
    return;
  }

  Serial.println("Client is ready");

  NimBLERemoteService* pSvc = pClient->getService(NimBLEUUID((uint16_t)0x1812));
  if (!pSvc) {
    Serial.println("HID service not found");
    pClient->disconnect();
    delay(100);
    resetBluetoothStack();
    return;
  }

  Serial.println("Get Characteristics");
  auto chars = pSvc->getCharacteristics(true);
  int subCount = 0;

  for (auto chr : chars) {
    if (chr->getUUID().equals(NimBLEUUID((uint16_t)0x2A4D)) && chr->canNotify()) {
      if (chr->subscribe(true, notifyCB)) {
        Serial.print("Subscribed to Handle: 0x");
        Serial.println(chr->getHandle(), HEX);
        ++subCount;
      } else {
        Serial.print("Failed to subscribe to Handle: 0x");
        Serial.println(chr->getHandle(), HEX);
      }
    }
  }

  if (subCount == 0) {
    Serial.println("No notifiable 0x2A4D characteristic found!");
    pClient->disconnect();
    delay(100);
    resetBluetoothStack();
    return;
  }

  isConnected = true;
}

int stopCounter = 0;     // global var
int in1 = 25;  // motorA
bool isDriverOn = false;
int state = 0; // 0 means stop, 1 will be forwards, 2 will be backwards, 3 will be left, and 4 will be right. 

// void driverOff(){
//     digitalWrite(27, LOW);  // eep
//     digitalWrite(2, LOW);
//     isDriverOn = false;
// }

// void driverOn(){
//     digitalWrite(27, HIGH);  // eep
//     digitalWrite(2, HIGH);
//     isDriverOn = true;
// }

void goForward() { // function that allows motors to move in forward direction
  // if(!isDriverOn){
  //   driverOn();
  // }
  digitalWrite(27, HIGH);
  analogWrite(17, 0); 
  analogWrite(16, 255);
  analogWrite(25, 255);
  analogWrite(26, 0);
}

void goBackward() { // function that allows motors to move in backward direction by swapping value from the previous function 
  //   if(!isDriverOn){
  //   driverOn();
  // }
  digitalWrite(27, HIGH);
  analogWrite(17, 255); 
  analogWrite(16, 0);
  analogWrite(25, 0);
  analogWrite(26, 255);
}

void goRight() {
  //   if(!isDriverOn){
  //   driverOn();
  // }
  digitalWrite(27, HIGH);
  analogWrite(17, 0);
  analogWrite(16, 255);
  analogWrite(25, 0);
  analogWrite(26, 255);
}

void goLeft() {
  //   if(!isDriverOn){
  //   driverOn();
  // }
   digitalWrite(27, HIGH);
  analogWrite(17, 255);
  analogWrite(16, 0);
  analogWrite(25, 255);
  analogWrite(26, 0);
}

void stopAll(){ // this function sets all movements to zero so motors stop. 
  //   if(!isDriverOn){
  //   driverOn();
  // }
  analogWrite(16, 0);
  analogWrite(17, 0);
  analogWrite(25, 0);
  analogWrite(26, 0);
  digitalWrite(27, LOW);
}




void setup(){
  Serial.begin(9600);
  delay(200);
  NimBLEDevice::init("");
  NimBLEDevice::deleteAllBonds();
  lastScanKickMs = millis();
  lastOnResultMs = millis();
  startScanNow();

  pinMode(2, OUTPUT);
  
  pinMode(27, OUTPUT);  // eep pin
  pinMode(26, OUTPUT);  // motorA
  pinMode(25, OUTPUT);  // motorB
  pinMode(16, OUTPUT);  // rx pin
  pinMode(17, OUTPUT);  // tx pin
  delay(10);
  // driverOn();

  digitalWrite(2, LOW);
}
void loop(){
  if (doConnect) {
    connectToServer();

  }
  if (isConnected) {
    digitalWrite(2, HIGH);
    if (currentCommand == FORWARD) {
      Serial.println("currentCommand == FORWARD");
      if(prevCommand != FORWARD){
        goForward();
      }
    } else if (currentCommand == BACKWARD) {
      Serial.println("currentCommand == BACKWARD");
      if(prevCommand != BACKWARD){
          goBackward();
      }
    } else if (currentCommand == LEFT) {
      Serial.println("currentCommand == LEFT");
      if(prevCommand != LEFT){
        goLeft();
      }
    } else if (currentCommand == RIGHT) {
      Serial.println("currentCommand == RIGHT");
      if(prevCommand != RIGHT) {
        goRight();
      }
    } else if (currentCommand == STOP) {
      Serial.println("currentCommand == STOP");
      if(prevCommand != STOP) {
        stopAll();
      }
    }
    prevCommand = currentCommand;
    delay(50);
  }
  uint32_t now = millis();
  if (!isConnected && !doConnect && (now - lastScanKickMs > 2000)) {
    lastScanKickMs = now;

    if (now - (uint32_t)lastOnResultMs > 6000) {
      Serial.println("WD: scan stuck -> reset BLE");
      resetBluetoothStack();
    } else {
      if (!NimBLEDevice::getScan()->isScanning()) {
        Serial.println("WD: scan not running -> restart");
        startScanNow();
      }
    }
  }

  
  delay(2);
}
