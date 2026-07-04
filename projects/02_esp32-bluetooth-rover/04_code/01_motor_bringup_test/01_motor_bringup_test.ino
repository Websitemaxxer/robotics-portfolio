int stopCounter = 0;     // global var
int in1 = 25;  // motorA
bool isDriverOn = false;
int state = 0; // 0 means stop, 1 will be forwards, 2 will be backwards, 3 will be left, and 4 will be right. 
void driverOff(){
    digitalWrite(27, LOW);  // eep
    digitalWrite(2, LOW);
    isDriverOn = false;
}

void driverOn(){
    digitalWrite(27, HIGH);  // eep
    digitalWrite(2, HIGH);
    isDriverOn = true;
}

void setup() {
  Serial.begin(9600);
  pinMode(2, OUTPUT);  // d2 which is the built in LED

  pinMode(27, OUTPUT);  // eep pin
  pinMode(26, OUTPUT);  // motorA
  pinMode(25, OUTPUT);  // motorB
  pinMode(16, OUTPUT);  // rx pin
  pinMode(17, OUTPUT);  // tx pin
  delay(10);
  driverOn();
}
void goForward() { // function that allows motors to move in forward direction
  if(!isDriverOn){
    driverOn();
  }
  analogWrite(17, 0); 
  analogWrite(16, 255);
  analogWrite(25, 255);
  analogWrite(26, 0);
}

void goBackward() { // function that allows motors to move in backward direction by swapping value from the previous function 
    if(!isDriverOn){
    driverOn();
  }
  analogWrite(17, 255); 
  analogWrite(16, 0);
  analogWrite(25, 0);
  analogWrite(26, 255);
}

void goLeft() {
    if(!isDriverOn){
    driverOn();
  }
  analogWrite(17, 0);
  analogWrite(16, 255);
  analogWrite(25, 0);
  analogWrite(26, 255);
}

void goRight() {
    if(!isDriverOn){
    driverOn();
  }
  analogWrite(17, 255);
  analogWrite(16, 0);
  analogWrite(25, 255);
  analogWrite(26, 0);
}

void stopAll(){ // this function sets all movements to zero so motors stop. 
    if(!isDriverOn){
    driverOn();
  }
  analogWrite(16, 0);
  analogWrite(17, 0);
  analogWrite(25, 0);
  analogWrite(26, 0);
}

void loop() {
  goForward();
  delay(10);
  stopAll();
  delay(10);
  goBackward();
  delay(10);

  stopCounter = stopCounter + 1;
  if (stopCounter > 1000) {
    stopCounter = stopCounter - 1;
    if(isDriverOn){
      driverOff();
    }
  
  }
}
