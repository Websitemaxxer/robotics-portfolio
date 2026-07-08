# Code — Arduino Starter Kit

**One folder per project/exercise.** Inside each folder I keep **two** sketches so my
own contribution is always visible:

- `*_base.ino` — the book's version, built as written (e.g. `blink_base.ino`)
- `*_mine.ino` — my modified/extended version (e.g. `blink_mine.ino`)

Keeping both side by side makes it obvious what came from the Arduino Projects Book and
what I changed or added myself. In each `*_mine.ino`, add a short comment at the top
saying **what you changed and why**.

## Layout

```
04_code/
├── exercise_01_blink/
│   ├── blink_base.ino     ← the book's version
│   └── blink_mine.ino     ← my modified version (e.g. Morse-code blink)
├── exercise_02_.../
│   ├── ..._base.ino
│   └── ..._mine.ino
└── ...
```

> `exercise_01_blink/` is included as an empty example folder — drop your `.ino` files
> in and delete its `.gitkeep`. Copy the same two-file pattern for each new exercise.

## Done so far

- **`exercise_02_spaceship_interface/spaceship_base.ino`** — Project 2, the version I
  actually built and ran (idle → green LED; button held → two red LEDs alternate). See
  the [build diary](../01_planning/BUILD_DIARY.md) for the debugging story and
  [wiring](../03_electronics/WIRING.md) for the pin map. *My extension
  (`spaceship_mine.ino`) is still to come — planned: speed up the alarm the longer the
  button is held.*
- **`exercise_03_love_o_meter/lovemeter_base.ino`** — Project 3, my first sensor build.
  Reads a TMP36 temperature sensor on A0 and lights three LEDs (pins 2/3/4) like a
  bar-graph thermometer, printing the live temperature to the Serial Monitor. *Planned
  extension (`lovemeter_mine.ino`): auto-calibrate the baseline temperature at startup
  instead of hardcoding 20 °C.*
- **`exercise_04_color_mixing_lamp/colormixing_base.ino`** — Project 4. Reads three
  photoresistors (A0/A1/A2) and drives an RGB LED with PWM on pins 9/10/11 so its colour
  follows the light. My hardest debug so far — inverted dividers and a shared common-ground
  fault (see the [build diary](../01_planning/BUILD_DIARY.md)). *Planned extension
  (`colormixing_mine.ino`): use `map()` to balance the three channels so the colours
  aren't skewed toward blue without the coloured gels.*
- **`exercise_05_mood_cue/moodcue_base.ino`** — Project 5, my first motor. Reads a
  potentiometer on A0 and positions a servo on pin 9 (`Servo` library), so the arm follows
  the knob. My longest debug — a floating pot, a fiddly servo connector, and wire-colour
  confusion, finally cracked by isolating the servo straight to the Arduino (see the
  [build diary](../01_planning/BUILD_DIARY.md)). *Planned extension (`moodcue_mine.ino`):
  add a paper "mood" dial and smooth/limit the motion in code.*
- **`exercise_06_light_theremin/theremin_base.ino`** — Project 6. A photoresistor on A0
  sets the pitch of a piezo on pin 8 (`tone()`), so waving a hand over the sensor plays it.
  The sketch auto-calibrates its light range for the first 5 seconds. Debug: a flat-0 sensor
  reading traced to a wrong resistor value in the divider (see the
  [build diary](../01_planning/BUILD_DIARY.md)). *Planned extension (`theremin_mine.ino`):
  a button to re-trigger calibration on demand instead of only at startup.*
- **`exercise_07_keyboard_instrument/keyboard_base.ino`** — Project 7. Four pushbuttons
  share one analog pin (A0) via a resistor ladder, so each key reads a distinct value and
  plays its own note on the piezo (pin 8). Debug: the breadboard spacing had to be exact so
  the ladder chained in series (see the [build diary](../01_planning/BUILD_DIARY.md)).
  *Planned extension (`keyboard_mine.ino`): add more keys/octaves by extending the ladder.*
- **`exercise_08_digital_hourglass/hourglass_base.ino`** — Project 8. Six LEDs (pins 2–7)
  light one at a time every `interval` using `millis()` timing, and a tilt switch on pin 8
  resets them — an LED sand timer. First use of non-blocking `millis()` timing so it can
  count *and* watch the switch at once. *Planned extension (`hourglass_mine.ino`): a knob
  to set the total timer length.*
- **`exercise_11_crystal_ball/crystalball_base.ino`** — Project 11, my first LCD. A 16×2
  screen (`LiquidCrystal`) shows a prompt and, when a tilt switch (pin 6) fires, prints a
  random magic-8-ball answer. Debug: a blank screen traced to the contrast pot (only one
  outer leg connected) by forcing Vo to GND (see the
  [build diary](../01_planning/BUILD_DIARY.md)). *(Projects 9 & 10 skipped — need a 9V
  battery.) Planned extension (`crystalball_mine.ino`): custom answers / a shake animation.*
- **`exercise_12_knock_lock/knocklock_base.ino`** — Project 12. A button locks a servo
  (pin 9) and 3 knocks on a piezo (A0, used as a sensor) unlock it, with red/green/yellow
  status LEDs. Debug: it cycled locked/unlocked on its own until I fixed two floating
  inputs — a 10 kΩ pull-down on the button and a 1 MΩ across the piezo (see the
  [build diary](../01_planning/BUILD_DIARY.md)). *Planned extension (`knocklock_mine.ino`):
  require a specific knock rhythm instead of just a count.*
- **`exercise_13_touchy_feely_lamp/touchlamp_base.ino`** — Project 13. Touch a metal pad
  (a 1 MΩ across pins 4/2, `CapacitiveSensor` library) and an LED on pin 12 lights.
  **My first code change:** the default `threshold` of 1000 never triggered on my setup,
  so I read the real values on Serial and lowered it to **50** to match (see the
  [build diary](../01_planning/BUILD_DIARY.md)). *Next: auto-calibrate the threshold at
  startup so it adapts to any pad.*
- **`exercise_14_tweak_the_logo/`** — Project 14, my first project that **talks to the
  computer.** Two files, because this project spans two machines:
  `tweaklogo_base.ino` (the book's Arduino sketch — reads a pot on A0 and `Serial.write()`s
  the value as a byte) and `tweaklogo_processing.pde` (the companion **Processing** sketch
  that runs on the laptop and colours a window). The hardware is trivial; the real work was
  **software** — quitting the Arduino IDE so Processing could own the serial port, and
  fixing the book's `Serial.list()[0]` port pick (it grabbed the Mac's Bluetooth port, not
  the Arduino). The pot's colour control never swept (its outer legs weren't both powered),
  so my Processing sketch **auto-cycles the hue** for a clean demo; the Arduino sketch is
  still the book's real pot-driven version (see the
  [build diary](../01_planning/BUILD_DIARY.md)). *Next: get the pot sweeping a full range,
  then switch the window back to reading the live serial byte so the knob drives the colour.*

