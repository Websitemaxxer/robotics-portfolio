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

