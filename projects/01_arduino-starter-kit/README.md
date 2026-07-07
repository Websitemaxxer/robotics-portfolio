# Arduino Starter Kit

> **Status:** In progress (7 / 15 projects) &nbsp;·&nbsp; **Difficulty:** Beginner
> **Started:** 2026-07-04 &nbsp;·&nbsp; **Last updated:** 2026-07-07

**Based on:** The Arduino Projects Book's 15 guided projects + my own extensions (labelled per entry).

*Building foundational embedded-C, breadboarding, and sensor skills with the official Arduino Starter Kit — the genuine Arduino-branded kit that ships with the Arduino Projects Book.*

![Hero photo](05_media/photos/HERO.jpg)
<!-- Take one strong "hero" photo of your build (e.g. the LCD or a wired circuit),
     save it as 05_media/photos/HERO.jpg, and it will appear above. -->

## About this project

I'm working through the **official Arduino Starter Kit** and the **Arduino Projects
Book** that comes with it, which walks through **15 guided projects** (from a blinking
LED up to circuits using sensors, motors, an LCD, and a small keyboard instrument).

My aim is not just to follow the book's instructions. For each project I first build
the guided version to learn the concept, then **extend selected projects with my own
modifications** — a different sensor, a behaviour change, extra logic — so this becomes
evidence of understanding rather than just copying. Every extension is **clearly
labelled as mine** in the build diary and in `04_code/` (base sketch vs my modified
version), so it's obvious what was the book's and what was my own contribution.

## Results at a glance

| Metric | Target | Achieved |
|--------|--------|----------|
| Guided projects completed (of 15) | 15 | 7 / 15 *(Spaceship Interface, Love-o-Meter, Color Mixing Lamp, Mood Cue, Light Theremin, Keyboard Instrument, Digital Hourglass)* |
| Self-designed extensions | ≥ 3 | 0 *(next: auto-calibrate the Love-o-Meter baseline)* |
| Sensors understood well enough to reuse in a future project | ≥ 3 | 2 *(TMP36 temperature sensor; photoresistor / LDR)* |

## What I did

- **The problem:** I'm new to embedded electronics and want a solid, hands-on foundation in circuits, breadboarding, and writing/uploading C/C++ to a microcontroller.
- **My contribution:** Beyond building each guided project, I extend selected ones with my own modifications (labelled per diary entry and per sketch in `04_code/`).
- **Adapted from source:** The base circuits and starter sketches come from the Arduino Projects Book; I keep the book's version alongside my modified version so the difference is visible.
- **Result so far:** Completed **Project 2 (Spaceship Interface)** — a pushbutton control panel that shows a steady green "idle" light and switches to alternating red "alarm" LEDs when pressed. It took **three separate wiring faults** to get working (a floating switch input, a half-seated +5 V jumper, and a signal wire in the wrong pin), all traced and documented in the [build diary](01_planning/BUILD_DIARY.md). Then **Project 3 (Love-o-Meter)** — my first **sensor** build, reading a TMP36 over analog input and lighting three LEDs like a thermometer; hit one backwards LED and fixed it in seconds because I'd already learned that failure mode. Then **Project 4 (Color Mixing Lamp)** — a hard debug: an RGB LED driven by PWM from three photoresistors, where I had to fix inverted voltage dividers *and* a shared common-ground fault, using the Serial Monitor to prove the input side was fine and isolate the problem to the output. Then **Project 5 (Mood Cue)** — my first **motor**: a potentiometer that positions a servo. This was my longest debug (~2.5 h) — a floating pot, a fiddly servo connector, wire-colour confusion, and repeated USB dropouts — cracked by **isolating the servo** (wiring it straight to the Arduino with a test sketch) to prove it was healthy and pin the fault on my breadboard wiring. Then **Project 6 (Light Theremin)** — making **sound** with `tone()`: a photoresistor whose light level sets the pitch. The pitch wouldn't respond until I traced a flat-0 sensor reading to a **wrong resistor value** in the divider — a good reminder to check a part's *value*, not just that it's plugged in. Then **Project 7 (Keyboard Instrument)** — four buttons sharing one analog pin via a **resistor ladder** to play four notes; the fix here was getting the breadboard **spacing** exactly right so the ladder chained in series and each key read a distinct value. Then **Project 8 (Digital Hourglass)** — an LED sand-timer that advances one LED per interval and resets on a tilt switch; a clean first-try build whose new idea was **`millis()` timing** (counting time *and* watching the switch at once, instead of freezing on `delay()`).

## Explore this project

- [Problem statement](01_planning/PROBLEM_STATEMENT.md)
- [Build plan](01_planning/BUILD_PLAN.md)
- [**Build diary**](01_planning/BUILD_DIARY.md) — the session-by-session log (start here to see how it went)
- [CAD](02_cad/)
- [Electronics — BOM](03_electronics/BOM.csv) & [wiring](03_electronics/WIRING.md)
- [Code](04_code/) — one folder per exercise, with the book's base sketch **and** my modified version
- [Media — photos](05_media/photos/) & [videos](05_media/videos/)
- [Test log](06_tests/TEST_LOG.md)
- [Reflection](07_reflection/REFLECTION.md)
- [Portfolio evidence checklist](PORTFOLIO_CHECKLIST.md)

## Quick facts

- **Hardware:** Official Arduino Starter Kit — Arduino Uno, breadboard, jumper wires, assorted sensors (light, temperature, etc.), DC motor & servo, LEDs, and a 16x2 LCD.
- **Software stack:** Arduino IDE, C/C++.
- **Cost:** ≈ AED 390 for the kit *(official Arduino Starter Kit K000007, UAE retail — adjust if you paid a different price)*
- **Time:** ~7.15 hours so far *(Project 2 ~2 h; Project 3 ~35 min; Project 4 ~45 min; Project 5 ~2.5 h; Project 6 ~35 min; Project 7 ~25 min; Project 8 ~25 min)*
