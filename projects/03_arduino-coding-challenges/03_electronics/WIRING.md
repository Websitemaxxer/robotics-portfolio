# Wiring — Arduino Coding Challenges

The circuits for these challenges are deliberately simple (usually one input and one
output), so each challenge just lists its **pin map** here rather than a drawn diagram.
No physical build is required — sketches are verified by code review and can be run in a
browser simulator (Wokwi / Tinkercad Circuits).

## Challenge 1 — Reaction Timer

### Pin map

| Component | Board pin | Notes |
|-----------|-----------|-------|
| LED (+ 220 Ω to GND) | D8 | the "GO" light |
| Pushbutton | D2 | 10 kΩ **pull-down** to GND, other side to +5 V (reads HIGH when pressed) |
| Serial | — | 9600 baud (prints the reaction time in ms) |

### Power

- **Supply:** USB 5 V — logic only (one LED + one button).
- **No physical build required:** verified by code review; optionally runnable in Wokwi / Tinkercad Circuits.

### Notes

- The button uses an external **pull-down** (same as the kit's Spaceship button), so the pin reads LOW when open and HIGH when pressed — which is what the sketch's logic assumes.
