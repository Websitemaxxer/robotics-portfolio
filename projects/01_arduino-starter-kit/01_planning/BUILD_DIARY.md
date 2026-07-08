# Build Diary — Arduino Starter Kit

**This is the most valuable file in the project.** Add a short entry **every time you work on this**, no matter how small the session. Keep the **newest entry at the TOP**, and be **honest about what failed** — a diary full of only successes is not believable and teaches you nothing. The failures, dead ends, and "oh, that's why" moments are exactly what makes a portfolio stand out.

> **Tip:** don't write the heading by hand. From the repo root run
> `./scripts/new_entry.sh <folder>` (e.g. `./scripts/new_entry.sh 01_arduino-starter-kit`)
> and it will insert a fresh, dated entry at the top for you to fill in.

---

## 2026-07-08 — Project 14: Tweak the Arduino Logo (my first project that talks to the computer)

- **Time spent:** ~50 minutes
- **Goal today:** Build Tweak the Arduino Logo — the Arduino reads a **potentiometer** and sends the value **over the USB/serial cable to the computer**, where a **Processing** sketch uses it to change the colour of a window on screen. This is the first project where the Arduino isn't the whole show: it's a **sensor feeding a program running on my laptop.**
- **What I did:** Wired a potentiometer to **A0** (wiper to A0, the two outer legs to +5 V and GND), uploaded the tiny Arduino sketch (`Serial.write(analogRead(A0) / 4)`), then installed **Processing** on the Mac and made a companion sketch to draw the colour window. Wrapped the whole thing up as a **one-click launcher** on the Desktop so it "just runs."
- **What worked:** The Arduino side works — the Serial Monitor fills with the live sensor bytes the moment it's plugged in (they show as odd symbols, which is correct — it's raw *data* for Processing, not text). And the Processing colour window runs and sweeps smoothly through the whole rainbow. Photos in `05_media/photos/`, demo clip in `05_media/videos/tweaklogo_demo.mp4`.
- **What failed / surprised me — this was the biggest problem of the whole kit so far.** The Arduino part was easy; getting **Processing** to actually run and read the Arduino turned into a long fight with the *software*, not the wiring:
  1. **"What even is Processing?"** — it's a separate program from the Arduino IDE. I had to install it, and at first **double-clicking my sketch did nothing** / the window wouldn't open.
  2. **The book's Processing code grabbed the wrong port.** It uses `Serial.list()[0]` — the *first* serial port — which on my Mac is a **Bluetooth** port, not the Arduino, so it errored out. The fix was to make it search the port list for the one containing **"usbmodem"** (the Arduino).
  3. **Two programs can't own the serial port at once.** Processing couldn't open the port because the **Arduino IDE's Serial Monitor still had it**. Just killing the helper didn't work — it respawns and re-grabs the port — so the real fix was to **quit the whole Arduino IDE** (the board keeps running the uploaded sketch on its own).
  4. **The knob didn't change the colour.** Even with everything talking, turning the pot did nothing on screen. The Serial values were stuck in a narrow band — the pot's **two outer legs weren't both getting power**, so the wiper had no voltage range to sweep (the *exact same* fault I'd hit on the Crystal Ball contrast pot). I proved it by uploading a quick sketch that prints all six analog pins as CSV and watching A0 barely move.
- **What I changed because of it:** Rewrote the Processing sketch to **auto-detect the "usbmodem" port** instead of blindly taking port 0; made the launcher **quit the Arduino IDE and free the port** before starting Processing; and, since the pot's colour control was the one thing I couldn't get stable, I made a version of the window that **cycles through the colours on its own** at a steady pace, so there's a clean, repeatable demo. Both ideas are captured: the Arduino sketch (`tweaklogo_base.ino`) is the book's real pot-controlled version, and `tweaklogo_processing.pde` is the self-cycling window.
- **Biggest lesson:** Once a project crosses onto the computer, a whole new class of bug appears that has nothing to do with the breadboard — **which** program owns the serial port, **which** port is even the right one, and whether the second program can get to it. Splitting "is the Arduino sending?" (yes — Serial Monitor proved it) from "is Processing receiving?" is the same *isolate-the-halves* habit as my hardware debugging, just applied to software.
- **Next step:** Project 15 (Hacking Buttons) — the last project in the book. (Projects 9 & 10 still waiting on a 9V battery.)
- **Photos:** [Finished build](../05_media/photos/tweaklogo_built.jpg) · [Wiring detail](../05_media/photos/tweaklogo_wired.jpg)

## 2026-07-08 — Project 13: Touchy-feely Lamp (a capacitive touch switch)

- **Time spent:** ~40 minutes
- **Goal today:** Build the Touchy-feely Lamp — touch a piece of metal and an LED turns on, using the **`CapacitiveSensor` library** to sense my finger's capacitance. No button, no moving parts — the metal *is* the switch.
- **What I did:** Wired the capacitive sensor (a **1 MΩ resistor between pins 4 and 2**, with a metal electrode on the pin-2 side) and an LED on pin 12. The sketch reads the capacitance and turns the LED on when the reading crosses a threshold.
- **What worked:** Touch the metal pad → LED on; let go → LED off, and the Serial number jumps up when I touch. Photos in `05_media/photos/`, demo clip in `05_media/videos/touchlamp_demo.mp4`.
- **What failed / surprised me:** A few things, and the last one was the real fix:
  1. **The LED was in backwards** — even when the sensor triggered, nothing lit. Flipped it and it came on.
  2. **I didn't get what "the pad" was** at first — it's just *any metal you touch* (I used a screw on a wire). It has to be **attached to the sensor wire** on the pin-2 side, and you touch it with a **bare finger** (your body's capacitance is what it senses — a screw alone does nothing).
  3. **Flaky connections** — it worked once then went dead. The capacitive sensor is super sensitive to a half-seated wire, so I had to reseat everything firmly.
  4. **The readings never reached the default threshold.** Even wired right, my touch values were way below the sketch's `threshold = 1000` — my pad/wire setup just reads smaller numbers. I watched the actual values on the Serial Monitor and **lowered the threshold to 50** to match, and it worked reliably.
- **What I changed because of it:** Flipped the LED, firmed up the wiring, and — my first real **code change** — lowered `threshold` from **1000 to 50** so it triggers on my actual touch readings.
- **Biggest lesson:** A threshold isn't one-size-fits-all. Capacitive readings depend on the pad size, wire length and surroundings, so you **read the real numbers** (untouched vs touched) and set the threshold **between** them. Tuning a constant to fit my own hardware is a small but real step from "copied the sketch" to "understood and adapted it."
- **Next step:** Project 14 (Tweak the Arduino Logo) — sending a sensor value to a Processing sketch on the computer.
- **Photos:** [Finished build](../05_media/photos/touchlamp_built.jpg) · [Wiring detail](../05_media/photos/touchlamp_wired.jpg)

## 2026-07-07 — Project 12: Knock Lock (a secret-knock safe)

- **Time spent:** ~50 minutes
- **Goal today:** Build the Knock Lock — press a button to **lock** a box (a servo turns the "latch", red LED on), then **knock a secret code** (3 knocks on a piezo) to **unlock** it (servo turns back, green LED on). The piezo is used as a **knock *sensor*** here, and the servo is the actual lock.
- **What I did:** Wired a piezo to A0 (knock input), a button to pin 2, three LEDs (yellow/green/red on pins 3/4/5) and the servo to pin 9. The sketch locks on a button press and unlocks after 3 valid knocks.
- **What worked:** In the end it locks on the button (green → red, servo turns), each valid knock flashes the yellow LED, and 3 knocks unlock it (back to green). Photo in `05_media/photos/`, demo clip in `05_media/videos/knocklock_demo.mp4`.
- **What failed / surprised me:** This one threw three separate problems:
  1. **Button press did nothing** — the red LED never came on and the Serial Monitor stayed silent on a press. The button wasn't registering because **pin 2 was floating** (no pull-down), same lesson as the Spaceship button.
  2. **A piezo leg snapped off.** One lead broke clean out of the piezo body. I field-repaired it by pushing a wire into the empty hole/pad and trimming the excess — it made contact and worked.
  3. **The box locked and unlocked itself over and over** — the Serial Monitor rapidly flipped between "locked!" and "unlocked!" on its own. **Two** floating inputs were picking up noise: pin 2 (switch) and A0 (piezo). Pin 2 kept auto-locking, and the noisy piezo kept faking 3 knocks to auto-unlock.
- **What I changed because of it:** Added a **10 kΩ pull-down** from pin 2 to GND (steadies the button) and a **1 MΩ resistor** across the piezo (A0 to GND, drains its charge so it reads clean). I fixed them **one at a time** — I unplugged the piezo first, added the 10 kΩ and confirmed the box sat calmly on "unlocked", then reconnected the piezo and added the 1 MΩ.
- **Biggest lesson:** Two different inputs, two different fixes — and the way to debug it was to **isolate one at a time** (unplug the piezo so only the button could act). A digital input needs a **pull-down** to not float; a piezo knock sensor needs a **big (1 MΩ) resistor across it** to drain its charge, or it reads noise as knocks.
- **Next step:** Project 13 (Touchy-feely Lamp) — a capacitive touch sensor (the CapacitiveSensor library is already installed).
- **Photos:** [Finished build](../05_media/photos/knocklock_built.jpg)

## 2026-07-07 — Project 11: Crystal Ball (my first LCD — a digital magic 8-ball)

> Note: I skipped Projects 9 and 10 (Motorized Pinwheel, Zoetrope) for now — they need a 9V battery I don't have yet. I'll come back to them.

- **Time spent:** ~1 hour
- **Goal today:** Build the Crystal Ball — a **16×2 LCD** that shows "Ask the Crystal Ball!", and when you **tilt it**, displays a random answer (Yes / No / Ask again / …) like a magic 8-ball. My first project with an **LCD screen** and the `LiquidCrystal` library.
- **What I did:** Wired the LCD's control and data lines to the Arduino (RS, E, D4–D7), a **tilt switch** on pin 6, and a **potentiometer** to set the LCD contrast. The sketch prints the prompt, then on each tilt picks a random reply and shows it.
- **What worked:** Once the contrast was sorted, the prompt shows on power-up and every tilt gives a fresh random answer. Photos in `05_media/photos/`, demo clip in `05_media/videos/crystalball_demo.mp4`.
- **What failed / surprised me:** The backlight came on but **nothing showed on the screen**, and turning the contrast **pot did nothing at all.** That "pot does nothing" was the clue. I ran a clean test: I disconnected the pot from the LCD's contrast pin (Vo) and jumpered **Vo straight to GND** to force maximum contrast — and text appeared instantly. That proved the LCD, its power, *and* all the data wiring were fine, and the **only** problem was the contrast pot. The pot did nothing because **only one of its two outer legs was connected**, so the wiper had no voltage range to sweep. Reconnecting *both* outer legs (one to +5 V, one to GND) brought the adjustable contrast back.
- **What made it hard:** the sheer **number of wires** — the LCD alone needs a dozen connections, so with the pot and tilt switch it was the most wire-dense build so far and genuinely confusing to keep track of what went where.
- **Biggest lesson:** For a blank LCD, **force Vo to GND** to test the display on its own — it isolates the screen from the contrast pot in seconds. And a potentiometer needs **both** outer legs connected to do anything; with only one, it's dead.
- **Next step:** Projects 9 & 10 need a 9V battery I don't have, so I'm moving on to Project 12 (Knock Lock).
- **Photos:** [Finished build](../05_media/photos/crystalball_built.jpg) · [Wiring detail](../05_media/photos/crystalball_wired.jpg)

## 2026-07-07 — Project 8: Digital Hourglass (an LED sand timer)

- **Time spent:** ~25 minutes
- **Goal today:** Build the Digital Hourglass — six LEDs that light up one at a time at a fixed interval (like sand piling up), which reset when you tilt the whole thing over, using a **tilt switch**. First project using **`millis()` timing** and a tilt switch.
- **What I did:** Wired six red LEDs to pins 2–7 (each through a resistor) and a tilt switch to pin 8. The sketch uses `millis()` to light the next LED every `interval`, and watches the tilt switch — when it flips, all LEDs clear and the timer restarts.
- **What worked:** Everything, first try — no debugging needed. The LEDs advance one by one over time, and tilting the board resets them, just like flipping a real hourglass. Photos in `05_media/photos/`, demo clip in `05_media/videos/hourglass_demo.mp4`.
- **What failed / surprised me:** Honestly nothing broke this time — a rare clean build. What made it smooth was that the pieces were all things I'd already met: driving LEDs on multiple pins (Spaceship), reading a switch (Spaceship's button), and a `for` loop to set up the pins. The one **new idea** was `millis()` — timing without `delay()`, so the board can watch the tilt switch *and* keep counting at the same time (a `delay()` would freeze it).
- **What I changed because of it:** Nothing wiring-wise. To *see* it work quickly I temporarily lowered the `interval` (it's 600000 ms = 10 minutes per LED in the book version) to a couple of seconds, watched the LEDs march, then set it back.
- **Biggest lesson:** `millis()` vs `delay()` — using `millis()` lets the program do timing *and* respond to input at once, instead of stopping dead. That's the first "real" programming pattern (non-blocking timing) rather than just wiring, and it'll matter for anything that has to do two things at once.
- **Next step:** Project 9 (Motorized Pinwheel) — driving a DC motor with a transistor.
- **Photos:** [Finished build](../05_media/photos/hourglass_built.jpg) · [Wiring detail](../05_media/photos/hourglass_wired.jpg)

## 2026-07-07 — Project 7: Keyboard Instrument (a 4-key mini piano)

- **Time spent:** ~25 minutes
- **Goal today:** Build the Keyboard Instrument — four pushbuttons that each play a different note on the piezo, using a **resistor ladder** so all four buttons share a single analog pin (A0). First time reading multiple buttons through one pin instead of one pin each.
- **What I did:** Wired four pushbuttons into a chain of resistors (the "ladder") feeding **A0**, and the piezo across **pin 8** and GND. Each button connects a different point of the ladder to A0, so pressing each one gives a distinct reading (~1023, ~1000, ~510, ~7) that the sketch turns into a note (C, D, E, F).
- **What worked:** Once wired right, each button plays its own note and releasing goes silent. The Serial Monitor shows the reading jump to a different value for each key. Photos in `05_media/photos/`, demo clip in `05_media/videos/keyboard_demo.mp4`.
- **What failed / surprised me:** My biggest problem was the **spacing on the breadboard** — I didn't line the buttons and resistors up in the right rows/columns, so the ladder wasn't actually chaining the resistors in series and the button readings came out wrong (buttons giving the same value or nothing). Once I fixed the layout so each resistor and button sat in the correct columns, the readings separated out properly.
- **What I changed because of it:** Re-placed the buttons and resistors with the correct spacing so the ladder formed a proper series chain into A0 — then each key read its own distinct value.
- **Biggest lesson:** On a breadboard, **spacing is wiring.** Two components a column off from where they should be makes a completely different circuit even though everything "looks" connected. Getting the ladder's columns exactly right is what made the four keys read as four separate values.
- **Next step:** Project 8 (Digital Hourglass) — an LED "sand timer" driven by a tilt switch and `millis()` timing.
- **Photos:** [Finished build](../05_media/photos/keyboard_built.jpg) · [Wiring detail](../05_media/photos/keyboard_wired.jpg)

## 2026-07-07 — Project 6: Light Theremin (playing sound with light)

- **Time spent:** ~35 minutes
- **Goal today:** Build the Light Theremin — a photoresistor whose light level sets the pitch of a tone from a piezo, so waving my hand over the sensor "plays" it like the sci-fi instrument. Back to sensors after the servo, and my first time making **sound** with `tone()`.
- **What I did:** Wired a photoresistor voltage divider into **A0** and a piezo across **pin 8** and GND. The sketch spends its first 5 seconds **auto-calibrating** (onboard LED on while it learns the darkest and brightest readings), then maps the live light level to a pitch of 50–4000 Hz.
- **What worked:** After fixing the sensor, waving my hand over the photoresistor sweeps the pitch up and down smoothly — a proper theremin swoop. Photos in `05_media/photos/`, demo clip in `05_media/videos/theremin_demo.mp4`.
- **What failed / surprised me:** At first the piezo made sound but the **pitch wouldn't change** no matter how I moved my hand. I checked the sensor with a little test sketch that prints `analogRead(A0)` — and it read a **flat 0**, never moving. That meant no voltage was reaching A0 through the sensor. The cause turned out to be a **wrong resistor value** in the divider — I'd grabbed the wrong one, so the divider wasn't working. Swapping in the correct resistor made the readings sweep properly.
- **What I changed because of it:** Replaced the resistor, confirmed the sensor swept its full range on the test sketch, then went back to the Theremin.
- **One thing that fooled me:** the Theremin sketch has **no Serial output**, so its Serial Monitor is always blank — I briefly thought *that* was the bug, but it's normal. The real diagnosis came from the separate test sketch. Also the **5-second calibration** matters: you have to wave your hand over the sensor (full dark to full bright) during the startup window, or the pitch range comes out too narrow.
- **Biggest lesson:** Check the *value* of a part, not just that something's plugged in. A resistor of the wrong value looks identical to the right one but quietly breaks the circuit — the flat-0 reading on the test sketch is what exposed it.
- **Next step:** Project 7 (Keyboard Instrument) — buttons and a resistor ladder read on one analog pin to play different notes.
- **Photos:** [Finished build](../05_media/photos/theremin_built.jpg) · [Wiring detail](../05_media/photos/theremin_wired.jpg)

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
