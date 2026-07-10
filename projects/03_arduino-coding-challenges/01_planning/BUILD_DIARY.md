# Build Diary — Arduino Coding Challenges

**This is the most valuable file in the project.** Add a short entry **every time you work on this**, no matter how small the session. Keep the **newest entry at the TOP**, and be **honest about what failed** — a diary full of only successes is not believable and teaches you nothing. The failures, dead ends, and "oh, that's why" moments are exactly what makes a portfolio stand out.

> **Tip:** don't write the heading by hand. From the repo root run
> `./scripts/new_entry.sh <folder>` (e.g. `./scripts/new_entry.sh 03_arduino-coding-challenges`)
> and it will insert a fresh, dated entry at the top for you to fill in.

---

## 2026-07-08 — Challenge 1: Reaction Timer (my first from-scratch sketch, no help)

- **Time spent:** ~40 minutes
- **Goal today:** Prove I can write a kit-level sketch from just a spec. The challenge: after a random 2–5 s wait an LED turns on; press a button as fast as possible; print the reaction time in ms; and catch a "false start" if the button is pressed before the LED. LED on **D8**, button on **D2** (10 kΩ pull-down), Serial at **9600**. No coding help — only the goal, behaviour and pins.
- **What I did:** Wrote the whole sketch myself from a blank file, had it reviewed, fixed every problem myself, then tidied it into a shorter final version.
- **What worked (in the end):** The finished sketch does all six requirements — random GO light, accurate reaction time, self-restarting rounds, and a "Too soon!" false-start. Code in `04_code/challenge_01_reaction_timer/`.
- **What failed / surprised me — my first attempt was rough, in two layers:**
  1. **It didn't even compile.** Three syntax mistakes: I wrote `void loop({` instead of `void loop() {`; I tried to put an `else` on a `while` loop (only an `if` can have an `else`); and I left a stray extra `)` at the very end. Pure bracket discipline.
  2. **Even fixed, the logic was wrong.** The big one: I used `millis()` as if it *reset* every round, comparing it to fixed numbers like `> 2000 && < 5000`. But `millis()` only counts *up* from power-on and never resets — so my "wait" block only ran once, and one of my `while` loops (`millis() > 5000`) became **true forever** and would freeze the whole program. On top of that I never actually *read* the button (my `switchState` stayed `0` the entire time), I tried to check if the LED was on with `ledPin == HIGH` (which just compares the number 8 to 1), and I printed `millis()` — total uptime — as the "reaction time" instead of a difference.
- **What I changed because of it:** Rewrote it around the right idea — a reaction time is a **difference between two timestamps**: save the moment the LED turns on (`start = millis()`), wait for the press, then `millis() - start`. Read the button properly with `digitalRead`, use `random(2000, 5001)` for the wait, poll the button *during* the wait to catch a false start, and use `return` to bail out and restart a cheated round. That version worked. Then I shortened it: instead of hand-counting elapsed time in 10 ms steps, set one deadline `waitUntil = millis() + random(...)` and loop until the clock passes it.
- **Biggest lesson:** `millis()` never resets — you can't compare it to fixed per-round numbers, you compare **timestamps to each other**. That single misunderstanding was behind half my bugs. It's the same non-blocking-timing idea as the kit's Digital Hourglass, but this time I had to reach for it from memory instead of copying it.
- **Next step:** Challenge 2 (to be set).
- **Photos:** none — this is a software-only challenge (optionally runnable in a Wokwi / Tinkercad simulation).

## YYYY-MM-DD — <what this session was about>

- **Time spent:** 
- **Goal today:** 
- **What I did:** 
- **What worked:** 
- **What failed / surprised me:** 
- **What I changed because of it:** 
- **Next step:** 
- **Photos:** (add images to 05_media/photos/ and link them here)
