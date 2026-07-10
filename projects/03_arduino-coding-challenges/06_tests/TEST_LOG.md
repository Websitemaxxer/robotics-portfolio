# Test Log — Arduino Coding Challenges

Each test records **numbers**, not just "it worked." A number you can compare against a
target is evidence; "it worked" is an opinion.

---

## Test 1 — Reaction Timer: behaviour matches the six requirements — 2026-07-08

- **Setup:** `04_code/challenge_01_reaction_timer/reaction_timer.ino` targeting an Arduino Uno (LED on D8, pushbutton on D2 with a 10 kΩ pull-down, Serial at 9600). Checked by reading the code line-by-line against the spec; it can also be run in a Wokwi / Tinkercad simulation. No physical board was on hand, so no measured reaction-time values are recorded yet.
- **Procedure:** Trace each of the six required behaviours through the code and confirm it does exactly that.
- **Result (requirement-by-requirement):**
  1. LED off at the start of each round — **PASS** (`digitalWrite(ledPin, LOW)` at the top of `loop()`).
  2. Random 2–5 s wait — **PASS** (`random(2000, 5001)` → 2000–5000 ms; upper bound is exclusive).
  3. LED on = GO, and the start time is captured then — **PASS** (`start = millis()` right after `HIGH`).
  4. Reaction time = press moment − GO moment, in ms — **PASS** (`millis() - start`).
  5. Rounds restart on their own — **PASS** (`loop()` repeats; `delay(1000)` between rounds).
  6. False start (press before GO) → "Too soon!" and restart — **PASS** (button polled during the wait; `return` restarts the round).
- **Pass / fail vs target:** Target = all six behaviours correct → **6 / 6 PASS** by code review.
- **What I'd change:** Run it in a simulator (or on the kit) to log real reaction-time numbers — a human is usually ~150–350 ms — and call `randomSeed()` once so the wait sequence differs each power-up instead of repeating.
