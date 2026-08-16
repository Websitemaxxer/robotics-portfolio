# Code: Arduino Starter Kit

One folder per project. Each keeps two sketches so my own contribution is clear:

- `*_base.ino`, the book's version, built as written.
- `*_mine.ino`, my modified or extended version (added where noted).

## Layout

```
04_code/
├── exercise_02_spaceship_interface/
│   ├── spaceship_base.ino   ← the book's version
│   └── spaceship_mine.ino   ← my modified version (when added)
├── coding_challenges/
│   └── challenge_01_reaction_timer/
└── ...
```

## Sketches

| Project | Sketch | What it does |
|---------|--------|--------------|
| 2 Spaceship Interface | `exercise_02_spaceship_interface/spaceship_base.ino` | Idle → green LED; button held → two red LEDs alternate |
| 3 Love-o-Meter | `exercise_03_love_o_meter/lovemeter_base.ino` | TMP36 on A0 lights three LEDs (D2/D3/D4) like a bar-graph thermometer, prints live temperature to Serial |
| 4 Color Mixing Lamp | `exercise_04_color_mixing_lamp/colormixing_base.ino` | Three photoresistors (A0/A1/A2) drive an RGB LED with PWM on D9/D10/D11 so its colour follows the light |
| 5 Mood Cue | `exercise_05_mood_cue/moodcue_base.ino` | Potentiometer on A0 positions a servo on D9 (`Servo` library) |
| 6 Light Theremin | `exercise_06_light_theremin/theremin_base.ino` | Photoresistor on A0 sets a piezo's pitch on D8 (`tone()`); auto-calibrates for the first 5 s |
| 7 Keyboard Instrument | `exercise_07_keyboard_instrument/keyboard_base.ino` | Four buttons share A0 via a resistor ladder, each plays its own note on the piezo (D8) |
| 8 Digital Hourglass | `exercise_08_digital_hourglass/hourglass_base.ino` | Six LEDs (D2-D7) light in turn every interval with `millis()`; a tilt switch (D8) resets them |
| 11 Crystal Ball | `exercise_11_crystal_ball/crystalball_base.ino` | 16×2 LCD (`LiquidCrystal`) shows a prompt, a tilt switch (D6) prints a random answer |
| 12 Knock Lock | `exercise_12_knock_lock/knocklock_base.ino` | Button locks a servo (D9), 3 knocks on a piezo (A0) unlock it, with red/green/yellow status LEDs |
| 13 Touchy-feely Lamp | `exercise_13_touchy_feely_lamp/touchlamp_base.ino` | Touch a metal pad (1 MΩ across D4/D2, `CapacitiveSensor`) to light an LED on D12; my first code change, `threshold` lowered to 50 |
| 14 Tweak the Logo | `exercise_14_tweak_the_logo/tweaklogo_base.ino` + `tweaklogo_processing.pde` | Arduino reads a pot on A0 and `Serial.write()`s the byte; a Processing sketch colours a window from it |

Projects 9 and 10 skipped (need a 9V battery). `*_mine.ino` extensions are planned per project but not yet added.

## Coding challenges

`coding_challenges/` holds self-set challenges (not book projects), each written from a blank file with no coding help, given only a goal, the behaviour, and the pins.

```
04_code/coding_challenges/
└── challenge_01_reaction_timer/
    └── reaction_timer.ino
```

| Challenge | Sketch | What it does |
|-----------|--------|--------------|
| 1 Reaction Timer | `challenge_01_reaction_timer/reaction_timer.ino` | After a random 2-5 s wait an LED (D8) turns on, press a button (D2) and Serial prints the reaction time in ms; a press before GO is a "Too soon!" false start. Exercises `millis()`, `random()`, digital I/O and `Serial`. |

First attempts, compile errors and fixes are in the [build diary](../01_planning/BUILD_DIARY.md).
