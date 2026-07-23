# Progress log

Concepts are marked done as they're completed — self-paced, no fixed schedule.

| Concept | Status | Notes |
|---------|--------|-------|
| Variables & types | ✅ Jul 12 | int/float/str/bool, `type()`, conversions, f-strings; read a NameError traceback |
| Functions | ⏭️ skipped | Known from prior experience — will be verified in the final assessment |
| Scope | ✅ Jul 13 | Local vs global names, `UnboundLocalError`, the `global` keyword vs returning values |
| Lists | ✅ Jul 14 | append/insert/remove, slicing incl. negative indices and `[::-1]`, `enumerate()` + unpacking; slices are copies |
| Dictionaries | ✅ Jul 14 | build/add/update, `in`, `.get()` with fallback, `.keys()/.values()/.items()`, `sum(values)`; understands KeyError + unpack ValueError |
| Tuples & sets | ✅ Jul 14 | Tuple unpacking + immutability (TypeError), set dedupe via `set()`, `len()`, membership `in` |
| Conditionals | ✅ Jul 14 | if/elif/else chains, compound `and`/`or`/`not`, bools used directly (no `== True`), elif inherits failed checks |
| Loops | ✅ Jul 14 | `for`+`range()`, `while` (counter: create/check/increase), `while True`+`break`, `continue` guard (first-try ✓, in portfolio), infinite-loop debugging |
| Comprehensions | ✅ Jul 14 | `[expr for x in list if cond]` as one-line build+filter; understands colon = block-opener rule |
| Reading tracebacks | ✅ Jul 14 | Bottom-up reading, error-name vocabulary; learned ValueError vs TypeError and NameError vs AttributeError distinctions the hard way |
| Debugging | ✅ Jul 14 | Checkpoint-print method: expect → inspect → fix above first mismatch; SyntaxError ≠ runtime bug. **Week 1 complete** |
| Modules & imports | | |
| Virtual environments | | |
| Text file I/O | | |
| CSV | | |
| JSON | | |
| Exceptions | | |
| Classes & `__init__` | | |
| Methods & `self` | | |
| `__repr__` | | |
| Composition | | |
| Class vs function judgment | | |
| Arrays vs lists (NumPy) | | |
| Indexing & slicing | | |
| Boolean masks | | |
| Vectorised ops | | |
| Aggregations | | |
| Matplotlib | | |
| Reading unfamiliar code | | |
| pyserial basics | | |
| Parsing serial data | | |
| Python → Arduino commands | | |
| Timing & blocking | | |
| State machine | | |
| Final synthesis build | | |

## Week 1 review — combined-concept exercises (Jul 18)

Mixed exercises that pull several Week 1 concepts into one program, stepping up in difficulty. Code in [`week1/`](week1/).

| Exercise | Result | Concepts combined | Notes |
|----------|--------|-------------------|-------|
| [Sensor check](week1/review_sensor_check.py) | Corrected | lists, enumerate, conditionals, comprehensions | Missed the position number; boundary used `> 20` so an exact 20 fell on the wrong side |
| [Battery levels](week1/review_battery_levels.py) | ✅ First try | lists, enumerate, conditionals, comprehensions | Boundary handled correctly; redundant `elif` tidied to `else` |
| [Motor report](week1/review_motor_report.py) | Corrected | dicts, `.items()`/`.values()`, conditionals, comprehensions, aggregation | Found the hottest motor with separate `max(values)` and `max(keys)` — `max` on keys ranks alphabetically, so name and temperature came from different motors. Fixed by tracking both together in the loop |

**Takeaway so far:** loop/conditional/comprehension mechanics are solid. The recurring gap is *boundary conditions* (which side `>=` puts the equal case on) and keeping related values paired when searching for a max/min.

## Accumulator-pattern drills (Jul 25)

Harder combined exercises focused on the **accumulator pattern** — creating a collection before a loop, filling it inside, using it after. Worked through nested-tuple servo/battery/wheel reports and record-grouping logs.

| Exercise | Concepts drilled |
|----------|------------------|
| [Drone log](week1/review_drone_log.py) | Grouping dict + counting dict + set dedupe in one loop, tuple unpacking, two-branch if/else, filtered comprehension, `max()` with `key`/`lambda`, empty-data guard |

**Recurring weak spots identified (revision targets):** (1) the accumulator pattern — before/inside/after loop placement; (2) treating a `(name, value)` tuple as if it were a bare number instead of unpacking it; (3) putting the right code in the right `if`/`else` branch; (4) choosing test data that would actually expose a bug, and exercising both branches. Verified working with both a full log and an empty log.

