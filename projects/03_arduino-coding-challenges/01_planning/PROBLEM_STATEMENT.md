# Problem Statement — Arduino Coding Challenges

## Intended user / purpose

For me — to prove I actually learned to *write* Arduino code during the Starter Kit,
not just wire up and run the book's sketches.

## The problem

Following a book's code teaches the concepts but hides whether I could produce them
myself. I want honest evidence that, given only a goal and the pin numbers, I can write
a correct kit-level sketch from a blank file.

## Measurable success criteria

- Each challenge is written **entirely by me** — no starter code, no snippets, no fixes handed over.
- Each challenge **passes a correctness review** (and/or runs correctly in a browser simulator) against the behaviour it was given.
- **Zero coding help** taken to reach a working version — a review may point out *that* something is wrong, but I find and make the fix.

## Constraints

- I don't always have the physical kit on hand, so sketches are verified by code review and can be run in Wokwi / Tinkercad Circuits rather than on a real board.
- Challenges stay at the **same level** as the Arduino Starter Kit (digital I/O, analog I/O, `millis()` timing, `Serial`, `tone()`, servo, LCD) — no new hardware concepts beyond the kit.

## System diagram

The circuits are trivial (typically one input + one output), so each challenge lists its
pin map in [`03_electronics/WIRING.md`](../03_electronics/WIRING.md) rather than a drawn diagram.
