# Portfolio Evidence Checklist — Arduino Coding Challenges

Tick each item once the evidence actually exists in the repo. The goal is that
someone can open this project and find proof of every claim. Each line says
**where** that evidence should live.

> This is a **software-only** project (self-set coding challenges), so the hardware-oriented
> items — CAD, a drawn system/wiring diagram, a physical demo video — are marked
> *not applicable*. Ticks reflect Challenge 1 (Reaction Timer).

## Core evidence

- [x] **Problem statement** — the rules I set myself + measurable success criteria → `01_planning/PROBLEM_STATEMENT.md`
- [ ] **System diagram** — *not applicable*; circuits are one-in/one-out and captured as pin maps → `03_electronics/WIRING.md`
- [x] **Build plan** — challenge-by-challenge plan → `01_planning/BUILD_PLAN.md`
- [ ] **CAD / version history** — *not applicable* (no mechanical parts) → `02_cad/`
- [x] **BOM with costs** — parts each challenge targets; all already owned (AED 0) → `03_electronics/BOM.csv`
- [x] **Wiring / pin map** → `03_electronics/WIRING.md`
- [x] **Code in the repo** — the actual sketches, written from scratch → `04_code/challenge_01_reaction_timer/`
- [x] **Dated build diary** — an entry per session → `01_planning/BUILD_DIARY.md`
- [x] **At least one documented failure + fix** — the first attempt's compile errors *and* the `millis()`-never-resets logic bug → `01_planning/BUILD_DIARY.md`
- [x] **Quantitative test results** — 6/6 requirement conformance by code review (real timing numbers pending a simulator run) → `06_tests/TEST_LOG.md`
- [ ] **Demo video** — *optional*; could add a short Wokwi/Tinkercad screen capture → `05_media/videos/`
- [x] **Reflection** — what was original vs adapted, hardest problem → `07_reflection/REFLECTION.md`

## Polish (do this before calling it "done")

- [x] `README.md` filled in with a **results table** that has real numbers *(hero photo N/A — no hardware)*
- [x] A **row for this project added to the top-level `README.md`** Projects table
- [x] The **Skills checklist in the top-level `README.md`** reviewed for anything this project now proves
