/*
  Project 14 - Tweak the Arduino Logo (Arduino side)
  The book's version, built as written.

  Reads a potentiometer on A0 (0-1023) and sends it over the serial
  port as a single byte (0-255) by dividing by 4. A Processing sketch
  on the computer reads that byte and uses it to set the background
  colour of a window - so turning the knob changes the colour on screen.

  Serial.write() sends the RAW byte value (not text), which is why the
  Serial Monitor shows odd symbols instead of numbers - that's normal
  and correct: it's data meant for Processing, not for a human to read.

  This example code is in the public domain.
*/

void setup() {

  Serial.begin(9600);
}

void loop() {

  Serial.write(analogRead(A0) / 4);
  delay(100);
}
