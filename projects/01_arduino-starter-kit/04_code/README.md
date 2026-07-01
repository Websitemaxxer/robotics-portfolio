# Code — Arduino Starter Kit

**One folder per project/exercise.** Inside each folder I keep **two** sketches so my
own contribution is always visible:

- `*_base.ino` — the book's version, built as written (e.g. `blink_base.ino`)
- `*_mine.ino` — my modified/extended version (e.g. `blink_mine.ino`)

Keeping both side by side makes it obvious what came from the Arduino Projects Book and
what I changed or added myself. In each `*_mine.ino`, add a short comment at the top
saying **what you changed and why**.

## Layout

```
04_code/
├── exercise_01_blink/
│   ├── blink_base.ino     ← the book's version
│   └── blink_mine.ino     ← my modified version (e.g. Morse-code blink)
├── exercise_02_.../
│   ├── ..._base.ino
│   └── ..._mine.ino
└── ...
```

> `exercise_01_blink/` is included as an empty example folder — drop your `.ino` files
> in and delete its `.gitkeep`. Copy the same two-file pattern for each new exercise.
