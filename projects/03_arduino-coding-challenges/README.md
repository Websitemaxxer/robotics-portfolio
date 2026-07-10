# Arduino Coding Challenges

> **Status:** In progress (1 challenge done) &nbsp;·&nbsp; **Difficulty:** Beginner
> **Started:** 2026-07-08 &nbsp;·&nbsp; **Last updated:** 2026-07-08

**Based on:** Original work — self-set challenges at the level of the Arduino Starter Kit, written from scratch with no coding help.

*After finishing all the Arduino Starter Kit builds, I wanted to prove to myself that I actually understood the **code**, not just the wiring. So I set myself small coding challenges at the same level as the kit — given only a goal, the required behaviour, and the pin numbers — and write every line myself, with no starter code, snippets, or fixes handed to me. Each one is reviewed only after I think it's finished.*

## The rules I set myself

- I get **only** the project goal, the exact behaviour, and the pin numbers.
- **No coding help** — no starter code, no function hints, no fixes. I write it all.
- After I think it works, it gets **reviewed** — bugs are pointed out, but I find and make the fix myself.
- I don't always have the kit on hand, so sketches are checked by code review and can be run in a browser simulator (Wokwi / Tinkercad Circuits) — no physical board required.

## Challenges so far

| # | Challenge | Concepts exercised | Status |
|---|-----------|--------------------|--------|
| 1 | Reaction Timer | `millis()` timing, `random()`, digital in/out, `Serial`, program flow | ✅ Working (self-solved) |

## Results at a glance

| Metric | Target | Achieved |
|--------|--------|----------|
| Challenges written entirely from scratch (no coding help) | all | 1 / 1 |
| Challenges passing a correctness review | all | 1 / 1 |
| Coding help taken to reach a working version | 0 | 0 *(review pointed out bugs; I fixed them myself)* |

## What I did

- **The problem:** I finished the kit's 15 builds, but following a book's code isn't the same as being able to write it. I wanted honest evidence that I can produce a working sketch from just a spec.
- **My contribution:** Every line of every challenge is mine. For Challenge 1 (Reaction Timer) I worked out how to measure a reaction (capture the "GO" moment, then subtract) and how to catch a false start — after a first attempt that didn't even compile.
- **Adapted from source:** Nothing copied. The final saved sketch for Challenge 1 is a shortened refactor of my own working version (the `millis() + random()` deadline trick came out of the review) — the logic was mine first.
- **Result:** 1 challenge done and passing review, solved without any code being written for me.

## Explore this project

- [Problem statement](01_planning/PROBLEM_STATEMENT.md)
- [Build plan](01_planning/BUILD_PLAN.md)
- [**Build diary**](01_planning/BUILD_DIARY.md) — the session-by-session log (start here to see how it went)
- [Electronics — BOM](03_electronics/BOM.csv) & [wiring / pin maps](03_electronics/WIRING.md)
- [Code](04_code/) — one folder per challenge, each the final working sketch I wrote from scratch
- [Test log](06_tests/TEST_LOG.md)
- [Reflection](07_reflection/REFLECTION.md)
- [Portfolio evidence checklist](PORTFOLIO_CHECKLIST.md)

## Quick facts

- **Target hardware:** Arduino Uno + one LED (D8) + one pushbutton (D2). Already owned in the Starter Kit; challenges are written and checked without needing a physical build (browser simulator optional).
- **Software stack:** Arduino IDE, C/C++.
- **Cost:** AED 0 — uses the kit I already own; no new parts.
- **Time:** ~40 minutes so far *(Challenge 1)*.
