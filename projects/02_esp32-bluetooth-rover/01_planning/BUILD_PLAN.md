# Build Plan — ESP32 Bluetooth Rover

Reconstructed from the order things actually happened (the two sketches are dated Feb 16 and
Feb 20, 2026, and the whole build wrapped up around Feb 23). This was a fast ~1-week hobby build.

| Stage | Goal | Done? | Notes |
|-------|------|:-----:|-------|
| 1 | Assemble tracked chassis (acrylic base + Technic tracks/sprockets + N20 motors) | ☑ | Two motors, one per track, for tank-style steering |
| 2 | Wire ESP32 → DRV8833 → motors; prove motion with a test sketch | ☑ | `01_motor_bringup_test` — no Bluetooth yet; confirmed H-bridge + PWM + the `EEP` enable pin |
| 3 | Get the ESP32 to connect to the Bluetooth ring over BLE | ☑ | Hardest part — pairing the ring and reading its HID reports |
| 4 | Decode ring gestures → drive commands; integrate with motor code | ☑ | `02_rover_ble_ring` — full firmware |
| 5 | Make the connection robust (auto-reconnect) and test driving | ☑ | Added a watchdog that re-scans / re-inits the BLE stack |

> **Plan vs reality:** the mechanical and motor-driver parts went quickly; the **Bluetooth**
> side was where the real time went (getting the ring to pair, then figuring out its report
> format). That's the interesting part of the story — see the [build diary](BUILD_DIARY.md).
