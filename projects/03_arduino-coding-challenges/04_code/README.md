# Code — Arduino Coding Challenges

**One folder per challenge.** Each folder holds the **final working sketch** for a
challenge I set myself and wrote **from a blank file** — no starter code, no snippets,
no fixes handed to me. The point of this project is that every line is mine.

The messy part — first attempts, compile errors, wrong logic and how I fixed them — is
recorded honestly in the [build diary](../01_planning/BUILD_DIARY.md), not hidden.

## Layout

```
04_code/
├── challenge_01_reaction_timer/
│   └── reaction_timer.ino
└── ...
```

## Done so far

- **`challenge_01_reaction_timer/reaction_timer.ino`** — Challenge 1. A reflex game:
  after a random 2–5 s wait an LED (D8) turns on, you press a button (D2) as fast as you
  can, and the Serial Monitor prints your reaction time in milliseconds; pressing before
  the LED is a false start ("Too soon!"). Exercises `millis()` timing, `random()`, digital
  in/out and `Serial`. My first attempt didn't compile *and* had a core `millis()` logic
  bug — the [build diary](../01_planning/BUILD_DIARY.md) tells that story. The saved sketch
  is a shortened refactor of my own working version (the `millis() + random()` deadline
  trick came out of the review).
