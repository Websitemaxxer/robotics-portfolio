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
