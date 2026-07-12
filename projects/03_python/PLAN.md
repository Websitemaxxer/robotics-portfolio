# 6-Week Python Plan — started July 12, 2026

**How this works:**
- Each week has concepts to learn. Daily lessons + exercises happen on request.
- **No tests during the 6 weeks.** All concept tests are taken at the end (final assessment below).
- Progress is logged to `robotics-portfolio/projects/03_python` on GitHub.

## Week 1 — Core fluency (Jul 12–18)

Variables & types · Functions · Scope · Lists · Dictionaries · Tuples & sets · Conditionals · Loops · Comprehensions · Reading tracebacks · Debugging

## Week 2 — Structure & I/O (Jul 19–25)

Modules & imports · Virtual environments · Text file I/O · CSV · JSON · Exceptions

## Week 3 — Objects (Jul 26–Aug 1)

Classes & `__init__` · Methods & `self` · `__repr__` · Composition · Class vs function judgment

## Week 4 — NumPy & data (Aug 2–8)

Arrays vs lists · Indexing & slicing · Boolean masks · Vectorised ops · Aggregations · Matplotlib · Reading unfamiliar code

## Week 5 — Hardware (Aug 9–15)

pyserial basics · Parsing serial data · Python → Arduino commands · Timing & blocking · State machines

## Week 6 — Synthesis (Aug 16–22)

Build one original program from a blank file combining at least three of: classes, file I/O, NumPy, serial, plotting. Runs end to end without copying from earlier projects.

---

# Final assessment — taken at the end of the 6 weeks

Every concept has a pass/fail test. All of these are done at the end, after Week 6.

## Core fluency
- [ ] **Variables & types** — program using an int, float, string, bool; convert between them; print each with `type()`
- [ ] **Functions** — function with two args + a default, returns a result; call it 3 ways (positional, keyword, default)
- [ ] **Scope** — same variable name inside & outside a function; predict output before running, confirm
- [ ] **Lists** — build, append, insert, remove, slice `[1:4]` and `[::-1]`, loop with `enumerate()`
- [ ] **Dictionaries** — build, add/update/delete a key, loop `.items()`, safe read with `.get()`
- [ ] **Tuples & sets** — one sentence on when to use each over a list; dedupe a list with a set
- [ ] **Conditionals** — if/elif/else chain with a compound `and`/`or`/`not` condition
- [ ] **Loops** — a for loop and a while loop with same output; use `break` and `continue` in one
- [ ] **Comprehensions** — rewrite a 4-line list-building loop as a one-line comprehension with a filter
- [ ] **Reading tracebacks** — trigger TypeError, IndexError, KeyError, AttributeError; explain each from the traceback
- [ ] **Debugging** — plant a bug in a 20-line program, find it with `print()` or `breakpoint()`, fix it

## Structure & I/O
- [ ] **Modules & imports** — split a program across two files; import a function between them
- [ ] **Virtual environments** — create a venv, activate, `pip install` one package, `pip freeze > requirements.txt`
- [ ] **Text file I/O** — write & read a file with `with open(...)`; one sentence on why `with`
- [ ] **CSV** — read a CSV into rows, process, write a new CSV with the `csv` module
- [ ] **JSON** — write a dict to `.json`, load it back; confirm round trip
- [ ] **Exceptions** — try/except catching a *specific* exception; raise your own with a custom message

## Objects
- [ ] **Classes & `__init__`** — class with params; two instances with independent state
- [ ] **Methods & `self`** — method that modifies its own attribute; one sentence on what `self` is
- [ ] **`__repr__`** — printing the object shows useful info, not a memory address
- [ ] **Composition** — a class holding instances of another class (Robot holding Motors)
- [ ] **Class vs function judgment** — argue which of two problems needs a class vs a function

## NumPy & data
- [ ] **Arrays vs lists** — create a NumPy array; one sentence on why over a list for sensor data
- [ ] **Indexing & slicing** — from a 2D array: element, row, column, sub-block
- [ ] **Boolean masks** — filter above a threshold with a mask, no loop
- [ ] **Vectorised ops** — add two arrays, multiply by a scalar, no loop
- [ ] **Aggregations** — mean/std/min/max, then along an axis of a 2D array
- [ ] **Matplotlib** — line graph with labels + title, saved to `.png`
- [ ] **Reading unfamiliar code** — diary paragraph on one file from the desk-manipulator repo

## Hardware
- [ ] **pyserial basics** — open port, print Arduino lines for 10s, close cleanly
- [ ] **Parsing serial data** — read bytes, decode, strip, convert to float/int
- [ ] **Python → Arduino commands** — send a command that does something physical
- [ ] **Timing & blocking** — why `time.sleep()` in a control loop is bad; loop timed with `time.time()`
- [ ] **State machine** — ≥3 states (IDLE → MOVING → STOPPED) with behavior driven by state

## Synthesis
- [ ] **Final build** — original program combining ≥3 of: classes, file I/O, NumPy, serial, plotting
