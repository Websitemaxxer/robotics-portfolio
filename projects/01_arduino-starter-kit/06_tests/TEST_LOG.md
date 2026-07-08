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

---

## Test 7 — Light Theremin: pitch tracks the light — 2026-07-07

- **Setup:** Project 6 circuit (photoresistor divider on A0, piezo on pin 8 to GND), `theremin_base.ino` uploaded. Board reset so the 5-second calibration runs; hand waved from full-dark to full-bright during the calibration window.
- **Procedure:** After the onboard LED turns off, move a hand over the sensor and listen to the piezo.
- **Result (numbers):** Pitch sweeps across the sketch's full **50 Hz → 4000 Hz** range as the light on the sensor changes — low pitch in shadow, high pitch in bright light. A separate diagnostic sketch confirmed the raw A0 reading sweeps its full range (it read a flat 0 before the resistor was fixed).
- **Pass / fail vs target:** Target = pitch changes smoothly with the light on the sensor → **PASS.**
- **What I'd change:** The pitch range depends on the 5-second calibration — a nice extension would be a button to re-trigger calibration on demand instead of only at startup.

---

## Test 8 — Keyboard Instrument: each button plays its own note — 2026-07-07

- **Setup:** Project 7 circuit (four pushbuttons feeding a resistor ladder into A0, piezo on pin 8), `keyboard_base.ino` uploaded, Serial Monitor at 9600 baud.
- **Procedure:** Press each of the four buttons in turn; read the `keyVal` printed for each and listen to the note.
- **Result (numbers):** Each button produced a distinct reading — roughly **1023 / 1000 / 510 / 7** — matching the four ranges in the sketch, and each played its own note (C / D / E / F). No button pressed = silence.
- **Pass / fail vs target:** Target = four buttons, four different notes, silence when released → **PASS.**
- **What I'd change:** If a button's real reading drifts outside its code range (resistor tolerance), widen that range to the value the Serial Monitor actually shows. As an extension, add more keys/octaves by extending the ladder.

---

## Test 9 — Digital Hourglass: LEDs advance and reset on tilt — 2026-07-07

- **Setup:** Project 8 circuit (six LEDs on pins 2–7, tilt switch on pin 8), `hourglass_base.ino` uploaded. For a quick test the `interval` was temporarily lowered from 600000 ms to ~2000 ms.
- **Procedure:** Watch the LEDs light up one by one over the interval, then tilt the board and confirm they clear and the count restarts.
- **Result (numbers):** With interval ≈ 2 s, an LED lit roughly every 2 seconds, advancing 1 → 6 across the row. Tilting the board turned all six LEDs off and restarted the sequence. At the book's 600000 ms that's one LED every 10 minutes (a 1-hour timer across 6 LEDs).
- **Pass / fail vs target:** Target = LEDs advance at a fixed interval and a tilt resets them → **PASS.**
- **What I'd change:** Make the interval a named value that's easy to change for different timer lengths — an extension could add a potentiometer to set the total time.

---

## Test 10 — Crystal Ball: prompt shows and a tilt gives a random answer — 2026-07-07

- **Setup:** Project 11 circuit (16×2 LCD on RS/E/D4–D7, tilt switch on pin 6, contrast pot on Vo), `crystalball_base.ino` uploaded. Contrast pot adjusted for readable text.
- **Procedure:** Power on and read the prompt; tilt the board several times and read each answer.
- **Result (numbers):** On startup the LCD shows the two-line prompt. Each tilt cleared the screen and displayed one of **8 possible random answers** — over ~10 tilts I saw several different replies, confirming the `random(8)` is being read and varied.
- **Pass / fail vs target:** Target = readable prompt on power-up, and a fresh random answer on each tilt → **PASS.**
- **Diagnostic that cracked it:** Screen was blank with the pot doing nothing → jumpering the LCD's Vo pin straight to GND forced max contrast and text appeared, proving the fault was purely the contrast pot (only one outer leg connected).
- **What I'd change:** Add more/custom answer phrases, or a "shake harder" animation — small code tweaks now that the LCD works.

---

## Test 11 — Knock Lock: lock on button, unlock on 3 knocks — 2026-07-07

- **Setup:** Project 12 circuit (piezo on A0 with 1 MΩ across it, button on pin 2 with 10 kΩ pull-down, LEDs on 3/4/5, servo on pin 9), `knocklock_base.ino` uploaded, Serial Monitor at 9600 baud.
- **Procedure:** Press the button to lock, then knock the piezo and count the knocks needed to unlock; watch the LEDs, servo, and Serial.
- **Result (numbers):** Press → **green off, red on**, servo turns to 90°, Serial "the box is locked!". Then **3 valid knocks** (each flashing the yellow LED and printing "Valid knock of value …", counting down "2 / 1 more knocks to go") → servo returns to 0°, **green on, red off**, Serial "the box is unlocked!".
- **Pass / fail vs target:** Target = button locks it, exactly 3 valid knocks unlock it → **PASS.**
- **Key debug:** Before the resistors, the Serial Monitor cycled between "locked!" and "unlocked!" continuously (both inputs floating). Adding a 10 kΩ pull-down (pin 2) and a 1 MΩ across the piezo (A0) stopped the false triggering. Isolated by unplugging the piezo to test the button side alone first.
- **What I'd change:** Tune `quietKnock`/`loudKnock` to my knock strength using the printed `value`; or require a specific knock *rhythm*, not just a count.

---

## Test 12 — Touchy-feely Lamp: touch turns the LED on — 2026-07-08

- **Setup:** Project 13 circuit (1 MΩ between pins 4 and 2, metal electrode on the pin-2 side, LED on pin 12), `touchlamp_base.ino` uploaded with `threshold` tuned to **50**, Serial Monitor at 9600 baud.
- **Procedure:** Read the untouched value, then touch the metal pad and read the touched value; check the LED.
- **Result (numbers):** Untouched the reading sat near **0–5**; touching the pad pushed it well above **50** (the tuned threshold), turning the LED **on**; releasing dropped it back and the LED off. The default threshold of **1000 never triggered** on this setup — the tuned value of 50 is what made it reliable.
- **Pass / fail vs target:** Target = touch the pad → LED on, release → off → **PASS.**
- **Key debug:** Readings were too small for the default `threshold = 1000` (they depend on pad/wire/surroundings). Read the real values on Serial and set the threshold between untouched and touched — a small self-made code change.
- **What I'd change:** Auto-calibrate the threshold at startup (like the Light Theremin), so it adapts to any pad without hand-editing the number.

---

## Test 13 — Tweak the Arduino Logo: Arduino sends serial data to the computer — 2026-07-08

- **Setup:** Project 14 circuit (potentiometer wiper → A0, outer legs to +5 V/GND), `tweaklogo_base.ino` uploaded, Serial Monitor at 9600 baud.
- **Procedure:** Plug in the board and watch the Serial Monitor to confirm the Arduino is streaming the sensor value out over the serial port.
- **Result (numbers):** The Serial Monitor immediately filled with a **continuous stream of bytes** (shown as symbols/garbled characters, because `Serial.write()` sends the *raw* 0–255 value, not text — that is the correct, expected output for this sketch). New data arrived about **every 100 ms** (the sketch's `delay(100)`), confirming the board is sending ~10 values/second.
- **Pass / fail vs target:** Target = the Arduino continuously transmits the sensor byte over serial → **PASS.**
- **What I'd change:** Nothing on the Arduino side — it does exactly what the book asks. The pot's control range never widened (its two outer legs weren't both powered), so the value stayed in a narrow band; the fix is to reseat both outer legs to +5 V and GND (same lesson as the Crystal Ball contrast pot).

---

## Test 14 — Tweak the Arduino Logo: Processing window renders on the computer — 2026-07-08

- **Setup:** Processing 4 installed on the Mac; `tweaklogo_processing.pde` run via a one-click Desktop launcher that first quits the Arduino IDE to free the serial port.
- **Procedure:** Launch the sketch and watch the window on screen.
- **Result (numbers):** A **400×300 window** opens and its background **sweeps through the full HSB hue range (0 → 255)**, one step per frame at ~60 fps — a complete colour cycle roughly every **4 seconds** — with a live "Hue = N" readout. Captured in `05_media/videos/tweaklogo_demo.mp4`.
- **Pass / fail vs target:** Target = a Processing window on the computer that changes colour, driven by the Arduino project → **PASS** (self-cycling colour window; the pot-driven version is the book's `tweaklogo_base.ino` + `Serial.list()` reader, which streamed data correctly but couldn't sweep because of the unpowered pot).
- **Key debug (software, not wiring):** three separate serial-port problems — (1) the book's `Serial.list()[0]` picked the Mac's **Bluetooth** port, fixed by searching for **"usbmodem"**; (2) the Arduino IDE's **Serial Monitor still owned the port**, fixed by quitting the whole IDE (the board keeps running its sketch); (3) getting Processing to launch at all from one click.
- **What I'd change:** Once the pot sweeps a full range, switch the window back to reading the live serial byte so the **knob** drives the colour (the book's intended behaviour) instead of the auto-cycle.
