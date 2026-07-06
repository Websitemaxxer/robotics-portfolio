# Wiring — Arduino Starter Kit

## Project 2 — Spaceship Interface

### Wiring reference

I don't have a formal schematic for this one yet — the photo of the finished, working
circuit doubles as the wiring reference for now:

> ![Spaceship Interface wiring](../05_media/photos/spaceship_wired.jpg)

*(Planned improvement: redraw this as a proper Fritzing schematic and save it as
`../05_media/photos/wiring_diagram.jpg`.)*

### Pin map

| Component | Board pin | Notes |
|-----------|-----------|-------|
| Green LED (+ 220 Ω to GND) | D3 | Digital output — on when idle |
| Red LED 1 (+ 220 Ω to GND) | D4 | Digital output — alarm |
| Red LED 2 (+ 220 Ω to GND) | D5 | Digital output — alarm (alternates with D4) |
| Pushbutton | D2 | Digital **input**; 10 kΩ **pull-down** to GND, other leg to +5 V |

Logic: D2 reads **LOW** when the button is open (pulled to ground) → green on.
Pressing connects D2 to +5 V → reads **HIGH** → green off, reds alternate.

### Power

- **Supply:** USB from the computer (5 V).
- **Voltage:** 5 V logic throughout — no separate/motor supply needed for this project.
- **Measured current draw:** not measured (no multimeter yet) — it's a handful of LEDs, so tens of mA.
- **Regulation notes:** Onboard 5 V regulator only. +5 V and GND run to the breadboard power rails; every LED and the pull-down share the common GND rail.

### Gotchas I hit

- **Floating switch input.** With the pull-down not doing its job, D2 read HIGH all the time, so the board thought the button was permanently pressed — the reds flashed on their own. Fixed by wiring the 10 kΩ properly from D2 to GND.
- **Half-seated jumper.** The +5 V wire feeding the button *looked* connected but wasn't pushed fully into the breadboard hole, so pressing did nothing. "Looks connected" ≠ "is connected."
- **Signal wire in the wrong pin.** One red never lit because its control wire was in **D7 instead of D5** — the sketch drove D5 correctly, but nothing was plugged in there. Moved it one pin over and it worked.
- **LED polarity.** Worth remembering: long leg (+) toward the resistor/pin, short leg (flat notch, −) toward GND. An LED in backwards simply stays dark.
