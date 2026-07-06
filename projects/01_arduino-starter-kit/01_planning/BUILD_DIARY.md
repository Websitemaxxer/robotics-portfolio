# Build Diary — Arduino Starter Kit

**This is the most valuable file in the project.** Add a short entry **every time you work on this**, no matter how small the session. Keep the **newest entry at the TOP**, and be **honest about what failed** — a diary full of only successes is not believable and teaches you nothing. The failures, dead ends, and "oh, that's why" moments are exactly what makes a portfolio stand out.

> **Tip:** don't write the heading by hand. From the repo root run
> `./scripts/new_entry.sh <folder>` (e.g. `./scripts/new_entry.sh 01_arduino-starter-kit`)
> and it will insert a fresh, dated entry at the top for you to fill in.

---

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
