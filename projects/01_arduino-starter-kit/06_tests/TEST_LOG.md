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

---

## Test 4 — Love-o-Meter: LED bar-graph responds to temperature — 2026-07-06

- **Setup:** Project 3 circuit (three red LEDs on D2/D3/D4, TMP36 sensor on A0), `lovemeter_base.ino` uploaded, Serial Monitor open at 9600 baud.
- **Procedure:** Note the resting LED count, then pinch the flat face of the TMP36 between two fingers for ~20 s and watch both the LEDs and the live temperature in the Serial Monitor; then release and let it cool.
- **Result (numbers):** As the temperature rose, the lit-LED count climbed in steps **0 → 1 → 2 → 3**, matching the sketch's thresholds (an extra LED at roughly +2, +4 and +6 °C above the baseline). On cooling, the count stepped back down. Serial printed a continuous temperature stream throughout.
- **Pass / fail vs target:** Target = more LEDs light as the sensor warms, fewer as it cools, with a live temperature readout → **PASS.**
- **What I'd change:** The baseline is hardcoded to 20 °C and my room is warmer, so it rests with an LED or two already lit. Tune `baselineTemp` to my measured room temperature (read it off the Serial Monitor) so "all off" is the true resting state — or auto-calibrate it at startup.

---

## Test 5 — Color Mixing Lamp: RGB LED tracks light on the sensors — 2026-07-06

- **Setup:** Project 4 circuit (RGB LED channels on PWM pins 9/10/11 via 220 Ω, common leg to GND; three photoresistor dividers with 10 kΩ on A0/A1/A2), `colormixing_base.ino` uploaded, Serial Monitor at 9600 baud.
- **Procedure:** Shine a white torch on the sensors and read the raw values; then cover each sensor one at a time and watch the RGB LED colour shift.
- **Result (numbers):** After correcting the dividers, raw values rose to **~1000** under the torch (up from ~50–96 when the dividers were wired inverted). Mapped value = raw ÷ 4 ≈ **250** per channel → near-full brightness. Covering a sensor dropped its channel and the colour shifted (e.g. covering the blue sensor moved the LED toward red/orange).
- **Pass / fail vs target:** Target = LED colour changes as the light on each sensor changes → **PASS.**
- **What I'd change:** With one white light and no coloured gels the mix skews **blue/purple** (blue sensor reads highest, green lowest). Balance the three channels with `map()`, or add the coloured gels, for the full colour range.

---

## Test 6 — Mood Cue: servo tracks the potentiometer — 2026-07-06

- **Setup:** Project 5 circuit (10 kΩ potentiometer wiper → A0, servo signal → pin 9, servo power/ground on the +5 V/GND rails, capacitor across the rails), `moodcue_base.ino` uploaded, Serial Monitor at 9600 baud.
- **Procedure:** Turn the knob slowly from one end to the other and watch both the Serial values and the servo arm.
- **Result (numbers):** `potVal` sweeps the full **0 → 1023**, `angle` maps to **0 → 179**, and the servo arm rotates to match across its whole range. Holds position steadily when the knob stops.
- **Pass / fail vs target:** Target = servo arm follows the knob smoothly across its full travel → **PASS.**
- **Isolation test (diagnostic):** Servo wired **straight to the Arduino** (no breadboard) with a sweep sketch confirmed the servo moves 0/90/180 on its own — proving the servo and code were healthy and the fault was in the breadboard wiring. Kept as a reusable `Servo_Test`.
- **What I'd change:** Add a paper "mood" dial behind the arm so it points at labelled moods — and as an extension, smooth the motion or add end-stops in code.
