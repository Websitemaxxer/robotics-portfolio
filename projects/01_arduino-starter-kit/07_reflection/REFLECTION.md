# Reflection — Arduino Starter Kit

Written at the end of the project, while it's fresh.

- **What was original?** What did I design, write, or figure out myself?
  > The debugging was mine on every build — tracing three separate wiring faults on the
  > Spaceship, isolating the servo on the Mood Cue, spotting the inverted dividers and
  > shared-ground fault on the Color Mixing Lamp, and forcing the LCD's Vo to GND to prove
  > the Crystal Ball's screen was fine. My first real **code** changes were tuning the
  > Touchy-feely Lamp's touch threshold to my own hardware and writing a Processing sketch
  > for Tweak the Arduino Logo that auto-detects the serial port and auto-cycles the colour.
  > Finally, the **post-kit coding challenges** (Reaction Timer) are written entirely by me
  > from a blank file, with no coding help.

- **What was adapted, and from where?** Kits, tutorials, open-source designs, code
  snippets — name them and link them.
  > The base circuits and starter sketches come from the **Arduino Projects Book** that
  > ships with the official Arduino Starter Kit. I kept the book's version of each sketch in
  > `04_code/` so it's always clear what was the book's and what I changed. The book's code
  > is public-domain example code.

- **Hardest problem + how I solved it.** The one that nearly stopped me.
  > The Mood Cue servo (~2.5 h). A floating pot, a servo connector that wouldn't grip,
  > wire-colour confusion and repeated USB dropouts all stacked up. What cracked it was
  > **isolating the servo** — wiring it straight to the Arduino with a tiny sweep sketch —
  > which proved the servo and code were healthy and pinned the fault on my breadboard
  > wiring. That "cut it down to the smallest version that can fail" habit then paid off on
  > every later build.

- **What I'd do differently next time.**
  > Check a part's *value*, not just that it's plugged in (a wrong resistor cost me time on
  > the Light Theremin), and reach for a quick diagnostic sketch sooner instead of staring
  > at the breadboard. On the software side: check my brackets before assuming a logic bug.

- **What transfers to the next project?** Skills, tools, or habits I'll reuse.
  > Non-blocking timing with `millis()` (compare timestamps, don't block); using the Serial
  > Monitor to split a problem into "is the input side fine?" vs "is the output side fine?";
  > pull-down resistors for floating inputs; and isolating a suspect part to test it alone.

- **What skills does this project prove?**
  > Building a circuit from a wiring diagram; reading analog and digital sensors and reacting
  > in code; driving LEDs (PWM), a servo, a piezo and a 16×2 LCD; `millis()` timing; serial
  > debugging and Arduino↔computer serial communication (Processing); and — from the coding
  > challenges — writing a working Arduino sketch from just a spec, with no help.
