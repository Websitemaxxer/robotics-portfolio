# Build Diary — Arduino Starter Kit

**This is the most valuable file in the project.** Add a short entry **every time you work on this**, no matter how small the session. Keep the **newest entry at the TOP**, and be **honest about what failed** — a diary full of only successes is not believable and teaches you nothing. The failures, dead ends, and "oh, that's why" moments are exactly what makes a portfolio stand out.

> **Tip:** don't write the heading by hand. From the repo root run
> `./scripts/new_entry.sh <folder>` (e.g. `./scripts/new_entry.sh 01_arduino-starter-kit`)
> and it will insert a fresh, dated entry at the top for you to fill in.

---

## 2026-07-06 — Project 5: Mood Cue (my first motor — and my longest debug)

- **Time spent:** ~2.5 hours
- **Goal today:** Build the Mood Cue — a potentiometer that sets the position of a **servo motor**, so turning the knob sweeps the servo arm from 0° to 180° (like a dial pointing at a "mood"). My first project with a **moving part** and the **`Servo` library**.
- **What I did:** Wired a 10 kΩ potentiometer into **A0**, a servo onto pin **9** with power and ground, and a capacitor across the power rails to steady the servo's current draw. The sketch reads the knob (0–1023) and `map()`s it to a servo angle (0–179).
- **What worked (eventually):** Turning the knob now sweeps the servo arm smoothly across its full range, with `potVal` and `angle` tracking live in the Serial Monitor. Photos in `05_media/photos/`, demo clip in `05_media/videos/moodcue_demo.mp4`.
- **What failed / surprised me:** This was my longest fight yet — several separate problems stacked up:
  1. **Frozen knob reading.** `potVal` sat stuck around 300 and ignored the knob — the classic "floating pin." My potentiometer wasn't wired as a proper divider: I had to get **both outer legs** to +5 V and GND and the **wiper (the lone single pin) to A0**. Once all three were right, it swept 0–1023.
  2. **The servo connector wouldn't grip.** The kit's snap-off header pins have one long and one short end, so whichever way I turned them one side was always loose. Switched to plugging **jumper wires straight into the servo's plug** — full-length metal on both ends — which held properly.
  3. **Wire-colour confusion.** My servo's colours didn't match the book's diagram, and I nearly wired the power wire to the signal pin. The rule that saved me: **the middle wire of a servo is always power**, whatever colour it is — go by position, not colour.
  4. **The USB port kept dropping** ("cannot open port…") from all the replugging — reseating the cable and re-picking the port fixed it each time.
  5. **The servo still wouldn't move** even after all that. So I **isolated it**: wired the servo straight into the Arduino (no breadboard, no pot) and ran a tiny sweep test sketch. It worked perfectly — which proved the servo *and* the code were fine, and the fault was in my **breadboard connections** all along.
- **What I changed because of it:** Once the isolation test proved the servo was healthy, I reconnected it to the **same power rails that were already running the pot** (which I knew were live), pushed every wire in firmly, and it finally followed the knob.
- **Biggest lesson:** When something won't work, **cut it down to the smallest possible version** to find out *which* part is broken. Wiring the servo straight to the Arduino instantly told me the servo and code were fine, so I stopped suspecting them and focused on the breadboard — where the real problem (loose/wrong connections) had been the whole time.
- **Next step:** Project 6 (Light Theremin) — back to sensors, using a photoresistor to control sound from a piezo.
- **Photos:** [Finished build](../05_media/photos/moodcue_built.jpg) · [Wiring detail](../05_media/photos/moodcue_wired.jpg)

## 2026-07-06 — Project 4: Color Mixing Lamp (my hardest debug so far)

- **Time spent:** ~45 minutes
- **Goal today:** Build the Color Mixing Lamp — three photoresistors each reading a light level and driving one channel (red / green / blue) of an **RGB LED** through PWM, so the LED's colour changes with the light hitting the sensors. First project using **PWM output** (`analogWrite`) and **three analog inputs** at once.
- **What I did:** Wired the RGB LED (three colour legs through 220 Ω resistors to PWM pins **9, 10, 11**, common leg to ground) and three photoresistor voltage dividers (each with a 10 kΩ resistor) into **A0, A1, A2**, then uploaded the sketch and watched the raw sensor values in the Serial Monitor.
- **What worked:** In the end it lights up and the colour shifts as I change the light on the sensors — I confirmed each channel by covering the sensors one at a time and watching the colour move. Demo clip in `05_media/videos/colormixing_demo.mp4`.
- **What failed / surprised me:** This took the most debugging yet, in layers:
  1. **Nothing lit at all.** But the Serial Monitor was printing and the numbers changed with light, so the sensors and code were clearly fine — the fault had to be on the **LED side**. I wrote a quick test sketch that drives the RGB LED directly (ignoring the sensors); it lit up, proving the LED, its resistors and pins 9/10/11 were all good.
  2. **So why dark in the real sketch?** The sensor readings were tiny — only **~50–96 even with a phone torch right on them** — so the LED was being told "barely on." The cause: my three photoresistor dividers were wired **backwards (inverted)**, so *more* light gave a *lower* reading. I swapped the photoresistor and the 10 kΩ resistor to opposite sides of each divider and the readings jumped to **~1000**.
  3. **Still dark even then.** Because *all three* colours were out together, I reasoned it had to be the part they share — the RGB LED's **common leg to ground**. I re-seated that common-ground connection and it finally lit.
  4. Somewhere in the middle the Arduino **dropped its USB port** ("cannot open port…") from all the plugging and unplugging — reseated the cable and re-picked the port to get it back.
- **Biggest lesson:** Split the problem in half. The Serial Monitor proved the input side worked, so I stopped staring at the sensors and focused on the output. And "all three channels dead at once" pointed straight at the **shared ground**, not any single wire.
- **One quirk (not a fault):** with a single white torch and no coloured gels, the LED mostly shows **blue/purple** — my blue sensor reads highest and green lowest, so the mix is skewed. Adding the gels (or rescaling the ranges in code) would give the full colour range.
- **Next step:** Project 5 (Mood Cue) — my first **servo/motor**. Possible extension here: use `map()` to balance the three channels so the colours aren't skewed without gels.
- **Photos:** [Finished build (LED lit purple)](../05_media/photos/colormixing_built.jpg) · [Wiring detail](../05_media/photos/colormixing_wired.jpg)

## 2026-07-06 — Project 3: Love-o-Meter (my first sensor build)

- **Time spent:** ~35 minutes
- **Goal today:** Build the Love-o-Meter — a TMP36 temperature sensor driving three red LEDs like a bar-graph thermometer: warm the sensor (pinch it between your fingers) and the LEDs light up one after another. My first project using an **analog sensor** and the **Serial Monitor** instead of a simple on/off input.
- **What I did:** Wired the three red LEDs (pins 2, 3, 4, each through its own 220 Ω resistor) and the TMP36 sensor to analog pin **A0**, uploaded the sketch, and opened the Serial Monitor at 9600 baud to watch the live temperature. The code lights 0, 1, 2 or 3 LEDs depending on how far the temperature climbs above a baseline.
- **What worked:** Once everything was seated properly it did exactly what it should — the LEDs step up one by one as the sensor warms and step back down as it cools, and the temperature readout in the Serial Monitor tracks it in real time. Photos in `05_media/photos/`, demo clip in `05_media/videos/lovemeter_demo.mp4`.
- **What failed / surprised me:** One of the three red LEDs simply wouldn't light while the other two did. Because I'd already met this exact failure on the Spaceship build, I recognised it straight away instead of hunting around — a dead LED sitting next to working ones almost always means it's in **backwards**.
- **What I changed because of it:** Pulled that LED out and flipped it so the **long leg (+)** faced the resistor/pin side and the **short leg (flat notch, −)** faced ground. It lit up immediately and the meter worked end to end.
- **Biggest lesson:** The fault that cost me a long time on the Spaceship project took seconds here — I knew the symptom (one LED dark while its neighbours work → check polarity first) and went straight to the fix. Good sign the debugging habits from the last build are actually sticking.
- **Next step:** Tune the baseline temperature to my room (it's hardcoded to 20 °C, which is cooler than here) — a natural first **extension** would be to auto-calibrate the baseline at startup. Then on to Project 4 (Color Mixing Lamp).
- **Photos:** [Finished build](../05_media/photos/lovemeter_built.jpg) · [Wiring detail](../05_media/photos/lovemeter_wired.jpg)

## 2026-07-06 — Project 2: Spaceship Interface (wiring + a lot of debugging)

- **Time spent:** ~2 hours (mostly debugging, not building)
- **Goal today:** Build the Spaceship Interface — a pushbutton that switches a control panel between a calm "green" state and an alarm "red" state, using one green LED, two red LEDs, a pushbutton and resistors on the breadboard.
- **What I did:** Wired the circuit on the breadboard (green LED on pin 3, two red LEDs on pins 4 and 5, pushbutton on pin 2 with a 10 kΩ pull-down resistor), then uploaded the sketch to the Arduino Uno. The intended behaviour: **button not pressed → green LED on**; **button held → green off, the two red LEDs alternate-flash** like an alarm.
- **What worked:** Once the wiring was right, it behaves exactly as intended — steady green when idle, and the two reds alternating roughly every quarter-second while the button is held. Photos in `05_media/photos/`, demo clip in `05_media/videos/spaceship_demo.mp4`.
- **What failed / surprised me:** Almost nothing worked first try. I hit **three separate faults** and had to isolate them one at a time:
  1. **Reds flashed on their own; green only flickered when I pressed the button** — the exact opposite of what I wanted. The cause was the switch input: without a proper connection to ground it was "floating," so the Arduino read the button as *permanently pressed*. My pull-down resistor wasn't doing its job.
  2. **After fixing that, the green stayed solid but pressing the button did nothing.** This one fooled me because everything *looked* connected — the jumper feeding +5 V to the button was only half-seated in the breadboard hole, so no voltage was actually reaching the switch. Reseating it fixed it instantly.
  3. **Then one of the two red LEDs stayed completely dark.** I worked through it methodically: checked the LED polarity (flipped it — no change), confirmed the resistor was actually 220 Ω (blue-body, red-red-black-black-brown), and finally traced the signal wire back to the board — it was plugged into **pin 7 instead of pin 5**. The code was driving pin 5 correctly the whole time; nothing was listening there.
- **What I changed because of it:** Corrected the pull-down so the switch reads LOW when open, reseated the +5 V jumper, and moved the signal wire from pin 7 to pin 5. To stop *guessing*, I also wrote two throwaway diagnostic sketches — one that echoes the button state to the onboard LED, and one that lights each pin in turn — so I could tell a wiring fault apart from a code fault. Deleted them once the circuit was proven.
- **Biggest lesson:** "Looks connected" is not "is connected." Two of my three faults were mechanical — a wire in the wrong hole and a wire not pushed in far enough — not code. A quick diagnostic sketch beats staring at the breadboard.
- **Next step:** Build my own extension (`spaceship_mine.ino`) — e.g. make the alarm flash faster the longer the button is held — then move on to Project 3 (Love-o-Meter), which introduces the first real sensor.
- **Photos:** [Finished build (hero)](../05_media/photos/HERO.jpg) · [Wiring detail](../05_media/photos/spaceship_wired.jpg)

## YYYY-MM-DD — <what this session was about>

- **Time spent:** 
- **Goal today:** 
- **What I did:** 
- **What worked:** 
- **What failed / surprised me:** 
- **What I changed because of it:** 
- **Next step:** 
- **Photos:** (add images to 05_media/photos/ and link them here)
