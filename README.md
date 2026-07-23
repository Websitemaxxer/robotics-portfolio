# Robotics Portfolio — Kush Kumar

An aspiring engineer keeping an honest, dated record of what I build, how it works, and what I learn when it breaks.

## Contact

| | |
|---|---|
| **Name** | Kush Kumar |
| **School** | Cranleigh Abu Dhabi |
| **Email** | k.kumar@ankvt.com |
| **GitHub** | https://github.com/Websitemaxxer/robotics-portfolio |

## Projects

| # | Project | What it does | Key skills | Status | Folder |
|---|---------|--------------|------------|--------|--------|
| 1 | Arduino Starter Kit | Learning core electronics & embedded C via guided builds | Arduino, C/C++, breadboarding, sensors | Complete | [projects/01_arduino-starter-kit/](projects/01_arduino-starter-kit/) |
| 2 | ESP32 Bluetooth Rover | Tracked rover driven wirelessly from a Bluetooth finger-ring, via an H-bridge & PWM | ESP32, Bluetooth LE (NimBLE), H-bridge/PWM, motor control | Complete | [projects/02_esp32-bluetooth-rover/](projects/02_esp32-bluetooth-rover/) |
| 3 | Python for Robotics | A structured Python course building toward controlling hardware from Python | Python, data structures, file I/O, NumPy, pyserial | Ongoing | [projects/03_python/](projects/03_python/) |

*New projects are added with `./scripts/new_project.sh` and get a new row here.*

## How to read a project

Every project follows the same layout, so you always know where to look:

```
projects/<name>/
├── README.md                 ← start here: what it is, results at a glance
├── PORTFOLIO_CHECKLIST.md    ← evidence checklist (what's done / still needed)
├── 01_planning/              ← problem statement, build plan, and the BUILD DIARY
├── 02_cad/                   ← CAD files / exported drawings
├── 03_electronics/           ← BOM (with costs) + wiring diagram & pin map
├── 04_code/                  ← the actual firmware/code
├── 05_media/                 ← photos/ and videos/ (hero shot, progress, demo)
├── 06_tests/                 ← TEST_LOG with measured numbers vs targets
└── 07_reflection/            ← what was original vs adapted, what I'd change
```

The single most valuable file in each project is `01_planning/BUILD_DIARY.md` — a dated, honest log written session by session.

## Skills (growing checklist)

I tick these off as projects prove them. Blanks are things I haven't done *yet*.

**Mechanical**
- [x] Read and modify a CAD model *(ESP32 Rover — Blender model of the chassis)*
- [ ] Design and 3D-print a custom part
- [x] Assemble a moving mechanism (gears / linkages / drivetrain) *(ESP32 Rover — Technic tracked drivetrain)*

**Electronics**
- [x] Build a circuit from a wiring diagram on a breadboard *(ESP32 Rover — Fritzing design)*
- [ ] Read a datasheet and wire a sensor correctly
- [ ] Measure voltage and current with a multimeter
- [x] Power a project safely (regulation, correct supply) *(ESP32 Rover — 9V pack, driver, switch, common ground)*

**Software**
- [x] Write and upload embedded C/C++ to a microcontroller *(ESP32 Rover)*
- [x] Read a sensor and react to it in code *(Arduino Love-o-Meter — TMP36 analog read → LED bar graph)*
- [x] Drive a motor / actuator from code *(ESP32 Rover — DRV8833 H-bridge + PWM; Arduino Mood Cue — servo)*
- [x] Debug with serial output *(ESP32 Rover — BLE/gesture logging)*

**Practice (how I work)**
- [ ] Keep a dated build diary for a whole project *(Arduino kit in progress — diary started)*
- [x] Document a real failure and the fix *(Arduino Spaceship — traced 3 wiring faults one by one)*
- [x] Record quantitative test results against a target *(Arduino Spaceship — pass/fail test log)*
- [x] Produce a short demo video *(Arduino Spaceship — demo clip)*

## A note on original vs adapted work

Some future projects will build on excellent open-source robotics designs — for example the **JPL Open Source Rover**, **MuSHR**, **Sawppy**, or the **Faze4** robot arm. When I do, I will **always clearly label what was original and what was adapted**, both in each project's `README.md` and in `07_reflection/REFLECTION.md`. Standing on the shoulders of open-source work is normal engineering; passing it off as fully my own is not.
