# Test Log: Arduino Starter Kit

Measured behaviour against target for each build. Projects 9 and 10 skipped (need a 9V battery).

| # | Date | Project | What was verified | Result | Pass/Fail |
|---|------|---------|-------------------|--------|-----------|
| 1 | 2026-07-06 | 2 Spaceship Interface | Idle state, button not pressed | Green LED solid, both reds off over 30 s | PASS |
| 2 | 2026-07-06 | 2 Spaceship Interface | Button-held alarm state | Green off, two reds alternate ~0.25 s each (~0.5 s cycle) | PASS |
| 3 | 2026-07-06 | Diagnostic | Switch pin reads via `digitalRead(2)` | Open reads 0 (LOW), pressed reads 1 (HIGH); confirmed the floating input before the pull-down fix | PASS (after wiring fix) |
| 4 | 2026-07-06 | 3 Love-o-Meter | LED bar-graph vs temperature | Lit-LED count steps 0 → 1 → 2 → 3 as it warms and back down on cooling; live temperature on Serial | PASS |
| 5 | 2026-07-06 | 4 Color Mixing Lamp | RGB LED tracks light on three sensors | Raw ~1000 under a torch, mapped ~250/channel; covering a sensor shifts the colour | PASS |
| 6 | 2026-07-06 | 5 Mood Cue | Servo tracks the potentiometer | `potVal` sweeps 0 → 1023, `angle` maps 0 → 179, servo follows and holds; servo isolated straight to the Arduino to confirm it and the code were healthy | PASS |
| 7 | 2026-07-07 | 6 Light Theremin | Pitch tracks the light | Pitch sweeps the full 50 → 4000 Hz range with light level | PASS |
| 8 | 2026-07-07 | 7 Keyboard Instrument | Each button plays its own note | Distinct readings ~1023 / 1000 / 510 / 7, four notes (C/D/E/F), silence when released | PASS |
| 9 | 2026-07-07 | 8 Digital Hourglass | LEDs advance and reset on tilt | LED lights every interval, advancing 1 → 6; a tilt clears all six and restarts (tested at ~2 s; book default 600000 ms = 10 min/LED) | PASS |
| 10 | 2026-07-07 | 11 Crystal Ball | Prompt on power-up, random answer on tilt | Two-line prompt on startup; each tilt shows one of 8 random answers; Vo forced to GND confirmed the fault was the contrast pot | PASS |
| 11 | 2026-07-07 | 12 Knock Lock | Lock on button, unlock on 3 knocks | Button → red on, servo 90°, "locked"; 3 valid knocks → green on, servo 0°, "unlocked" | PASS |
| 12 | 2026-07-08 | 13 Touchy-feely Lamp | Touch turns the LED on | Untouched ~0-5, touch pushes above the tuned threshold of 50 and lights the LED (default 1000 never triggered) | PASS |
| 13 | 2026-07-08 | 14 Tweak the Logo | Arduino streams serial data | Continuous byte stream (raw `Serial.write()`, shown as symbols) about every 100 ms (~10 values/s) | PASS |
| 14 | 2026-07-08 | 14 Tweak the Logo | Processing window renders on the computer | 400×300 window sweeps the full HSB hue range (0 → 255), a full cycle ~4 s at ~60 fps | PASS |
| 15 | 2026-07-08 | Coding challenge 1: Reaction Timer | Six required behaviours, self-set challenge | Compiles cleanly (2978 bytes, 9% storage) for `arduino:avr:uno`; all six behaviours trace correctly | 6/6 PASS |

## Reaction Timer requirement check (Test 15)

| # | Requirement | In code |
|---|-------------|---------|
| 1 | LED off at the start of each round | `digitalWrite(ledPin, LOW)` at top of `loop()` |
| 2 | Random 2-5 s wait | `random(2000, 5001)` (upper bound exclusive) |
| 3 | LED on = GO, start time captured then | `start = millis()` right after `HIGH` |
| 4 | Reaction time = press moment - GO moment (ms) | `millis() - start` |
| 5 | Rounds restart on their own | `loop()` repeats, `delay(1000)` between rounds |
| 6 | False start → "Too soon!" and restart | Button polled during the wait, `return` restarts the round |
