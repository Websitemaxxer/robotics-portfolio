# Portfolio Evidence Checklist — ESP32 Bluetooth Rover

Tick each item once the evidence actually exists in the repo. The goal is that
someone can open this project and find proof of every claim. Each line says
**where** that evidence should live.

## Core evidence

- [x] **Problem statement** — who it's for, the problem, measurable success criteria → `01_planning/PROBLEM_STATEMENT.md`
- [ ] **System diagram** — described in the problem statement, but still needs an actual image (export the Fritzing or photograph a hand sketch) → `05_media/photos/`
- [x] **Build plan** — week-by-week plan → `01_planning/BUILD_PLAN.md`
- [x] **CAD / version history** — Blender model of the rover → `02_cad/rover_model.blend`
- [x] **BOM with costs** — all parts listed; total ≈150 AED (add per-item prices if you have them) → `03_electronics/BOM.csv`
- [x] **Wiring diagram + pin map** — pin map complete; Fritzing source included. *Still to do: export the `.fzz` to an image* → `03_electronics/WIRING.md`
- [x] **Code in the repo** — both sketches, with a walkthrough → `04_code/`
- [x] **Dated build diary** — one entry per session (reconstructed; add the personal details) → `01_planning/BUILD_DIARY.md`
- [x] **At least one documented failure + fix** — the flaky BLE connection → the reconnect/reset watchdog → `01_planning/BUILD_DIARY.md`
- [~] **Quantitative test results** — pass/fail recorded; a few real numbers (speed, range, current) still to measure → `06_tests/TEST_LOG.md`
- [x] **Demo video** — 20-second clip driving it with the ring → `05_media/videos/rover_demo.mov`
- [x] **Reflection** — original vs adapted, what I'd change → `07_reflection/REFLECTION.md`

## Polish (do this before calling it "done")

- [x] `README.md` filled in with a **results table** and a **hero photo** (a still from the demo video)
- [x] A **row for this project added to the top-level `README.md`** Projects table
- [x] The **Skills checklist in the top-level `README.md`** updated to tick what this project proves

## What's left for you (quick wins)

1. The hero image is a still pulled from the demo video. If you'd prefer the clean top-down
   photo you took, save it as `05_media/photos/HERO.jpg` (overwriting the current one) — or send
   it to me and I'll swap it in.
2. Optionally take the **measurements** noted in the test log — a nice-to-have, not a blocker.
3. Optionally export the Fritzing circuit to an image for the wiring diagram / system diagram.
