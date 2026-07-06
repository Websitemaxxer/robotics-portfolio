# Test Log — Arduino Starter Kit

Each test records **numbers**, not just "it worked." A number you can compare against a
target is evidence; "it worked" is an opinion. Repeat the block below for every test.

---

## Test 1 — Spaceship Interface: idle state — 2026-07-06

- **Setup:** Arduino Uno, breadboard circuit for Project 2 (green LED on D3, red LEDs on D4/D5, pushbutton on D2 with 10 kΩ pull-down). `spaceship_base.ino` uploaded. Button **not** pressed.
- **Procedure:** Power the board over USB, leave the button untouched, observe the three LEDs for 30 s.
- **Result (numbers):** Green LED on 100% of the time; both red LEDs off (0 flashes) over the 30 s window.
- **Pass / fail vs target:** Target = green solid, both reds off → **PASS.**
- **What I'd change:** Nothing for the guided version; behaviour is correct.

---

## Test 2 — Spaceship Interface: button-held alarm state — 2026-07-06

- **Setup:** Same circuit as Test 1. Button held down continuously.
- **Procedure:** Hold the pushbutton and watch the LEDs; time the alternation against a stopwatch over 10 cycles.
- **Result (numbers):** Green LED off; the two red LEDs alternate — each red on for ~0.25 s, giving a full A→B→A cycle of ~0.5 s (matches the two `delay(250)` calls in the sketch). Measured ~10 cycles in ~5 s.
- **Pass / fail vs target:** Target = green off, reds alternate roughly every quarter-second → **PASS.**
- **What I'd change:** For my own extension, make the alternation speed up the longer the button is held, instead of a fixed 250 ms.

---

## Test 3 — Switch input sanity check (diagnostic) — 2026-07-06

- **Setup:** Temporary diagnostic sketch echoing `digitalRead(2)` to the onboard LED and Serial Monitor (deleted after use).
- **Procedure:** Read the switch pin with the button open, then pressed, and check the reported state.
- **Result (numbers):** Button open → reads **0** (LOW); button pressed → reads **1** (HIGH). Before fixing the pull-down wiring it read **1** even when open — this test is what confirmed the input was floating.
- **Pass / fail vs target:** Target = 0 when open, 1 when pressed → **PASS** (after the wiring fix).
- **What I'd change:** Keep a small reusable "read one pin" diagnostic sketch on hand for future projects — it turned guesswork into a clear yes/no.
