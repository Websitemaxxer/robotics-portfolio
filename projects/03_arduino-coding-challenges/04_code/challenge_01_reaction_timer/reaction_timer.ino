/*
  Reaction Timer  (post-kit coding challenge #1)

  A reflex game: after a random 2-5 second wait the LED turns on (GO!),
  and you press the button as fast as you can. The Serial Monitor prints
  your reaction time in milliseconds. Pressing before the LED comes on is
  a false start ("Too soon!") and restarts the round.

  Pins:
    LED (+ 220 ohm to GND) ... D8
    Pushbutton ............... D2  (10k pull-down to GND, other side to +5V)
    Serial ................... 9600 baud
*/

int ledPin = 8;
int buttonPin = 2;

void setup() {
  pinMode(ledPin, OUTPUT);
  pinMode(buttonPin, INPUT);
  Serial.begin(9600);
}

void loop() {
  digitalWrite(ledPin, LOW);

  long waitUntil = millis() + random(2000, 5001);   // pick the GO moment once
  while (millis() < waitUntil) {                     // wait, watching for a cheat
    if (digitalRead(buttonPin) == HIGH) {
      Serial.println("Too soon!");
      delay(1000);
      return;
    }
  }

  digitalWrite(ledPin, HIGH);
  long start = millis();
  while (digitalRead(buttonPin) == LOW) { }          // wait for the real press
  Serial.print("Reaction time: ");
  Serial.print(millis() - start);
  Serial.println(" ms");

  delay(1000);
}
