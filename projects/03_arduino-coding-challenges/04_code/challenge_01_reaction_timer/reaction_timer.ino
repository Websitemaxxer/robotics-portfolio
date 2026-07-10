int ledPin = 8;
int buttonPin = 2;

void setup() {
  pinMode(ledPin, OUTPUT);
  pinMode(buttonPin, INPUT);
  Serial.begin(9600);
}

void loop() {
  digitalWrite(ledPin, LOW);

  long waitUntil = millis() + random(2000, 5001);
  while (millis() < waitUntil) {
    if (digitalRead(buttonPin) == HIGH) {
      Serial.println("Too soon!");
      delay(1000);
      return;
    }
  }

  digitalWrite(ledPin, HIGH);
  long start = millis();
  while (digitalRead(buttonPin) == LOW) { }
  Serial.print("Reaction time: ");
  Serial.print(millis() - start);
  Serial.println(" ms");

  delay(1000);
}
