/*
  Project 14 - Tweak the Arduino Logo (Processing companion)
  Auto-cycling version: the background hue sweeps through the colour spectrum
  on its own at a semi-fast pace. No serial/pot needed - it just runs.
  This example code is in the public domain.
*/

int hue = 0;

void setup() {
  size(400, 300);
  surface.setResizable(true);
  colorMode(HSB, 255);
  frameRate(60);
}

void draw() {
  hue = (hue + 1) % 256;          // step the hue each frame (~4s per full cycle)
  background(hue, 255, 255);

  fill(0, 0, 255);                // white text (HSB)
  textAlign(CENTER, CENTER);
  textSize(22);
  text("Hue = " + hue, width / 2, height / 2);
}
