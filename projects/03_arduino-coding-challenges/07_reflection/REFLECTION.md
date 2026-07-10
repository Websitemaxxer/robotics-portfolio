# Reflection — Arduino Coding Challenges

Written after Challenge 1. I'll add to it as more challenges are done.

- **What was original?** All of it. The challenge is set up so nobody writes the code for
  me — I get a spec and the pins, nothing else. For Challenge 1 I worked out the
  reaction-timing logic and the false-start handling myself.
  > Original.

- **What was adapted, and from where?** No code was copied. The saved version of Challenge 1
  is a shortened refactor of my own working sketch — the `millis() + random()` "deadline"
  tidy-up came out of the post-solve review — but the working logic was mine first.
  > A refactor of my own code; no external source.

- **Hardest problem + how I solved it.** Realising `millis()` never resets. My first attempt
  compared it to fixed per-round numbers, which made the timing block run only once and
  turned one loop into an infinite freeze. The fix was to think in **timestamp differences** —
  save when the LED lit, subtract that from the press time — which also fixed how I measured
  the reaction itself.

- **What I'd do differently next time.** Check my brackets/syntax before assuming the logic is
  the problem (my first attempt didn't even compile), and seed `random()` so the game isn't
  identical every power-up.

- **What transfers to the next project?** Non-blocking timing with `millis()` (compare
  timestamps, don't block), reading inputs with `digitalRead`, and using `Serial` to prove
  behaviour. Same tools as the kit, but now reached for from memory.

- **What skills does this project prove?** Writing and structuring an Arduino sketch from a
  blank file; timing with `millis()`; digital input/output; debugging from a correctness
  review; serial-based verification.
