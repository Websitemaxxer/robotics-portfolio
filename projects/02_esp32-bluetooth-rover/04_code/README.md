# Code — ESP32 Bluetooth Rover

Two sketches, in the order they were written. Each folder is a self-contained Arduino
sketch (the `.ino` matches its folder name, so it opens directly in the Arduino IDE).

> Original filenames were `sketch_feb16a.ino` and `sketch_feb20a.ino`. They were renamed
> for clarity when added to the portfolio — **the code itself is unchanged.**

## `01_motor_bringup_test/` — H-bridge + PWM bring-up (first)

The first thing I wrote: a no-Bluetooth test to prove the motor wiring and the
**DRV8833** H-bridge worked before adding any wireless control.

- Enables the driver by pulling the DRV8833 `nSLEEP` pin (GPIO27, labelled `eep` in code) HIGH.
- Defines `goForward()`, `goBackward()`, `goLeft()`, `goRight()`, `stopAll()` — each sets
  the four motor-input pins with `analogWrite()` (**PWM**). Direction on each motor is set
  by which of its two inputs is driven and which is held at 0; speed is the PWM value (0–255).
- `loop()` just cycles forward → stop → backward on a short delay to confirm both motors
  spin in both directions.

This is the classic **H-bridge** idea: two inputs per motor, and swapping which one is
"high" reverses the current through the motor, reversing its spin.

## `02_rover_ble_ring/` — full rover firmware (BLE ring control)

The complete rover firmware. It uses the **NimBLE-Arduino** library to talk to a
Bluetooth smart ring and turn its gestures into driving commands.

**How it works, end to end:**

1. **Scan & match** — scans for BLE devices advertising the HID service (`0x1812`) and
   matches the ring by its MAC address (`targetAddrStr`).
2. **Connect & subscribe** — connects as a BLE client, finds the HID Report characteristic
   (`0x2A4D`), and subscribes to its notifications.
3. **Decode gestures** (`notifyCB`) — parses each 8-byte HID report: a "button/active"
   flag, a gesture *group* id, and signed 16-bit X/Y values. On finger-release it compares
   the first vs last X/Y to decide the gesture:
   - horizontal swipe → `LEFT` / `RIGHT`
   - vertical swipe → `FORWARD` / `BACKWARD`
   - tap / specific group → `STOP`
4. **Drive** — `loop()` maps the current command to the same H-bridge motor functions from
   the bring-up sketch (differential/tank steering: turning drives the two sides in opposite
   directions). It only re-issues motor writes when the command *changes*, and lights the
   onboard LED (GPIO2) while connected.
5. **Self-healing BLE** — a small watchdog restarts scanning, and fully re-initialises the
   BLE stack, if the connection drops or scanning gets stuck. This is what makes it reliable
   enough to actually drive around.

### Library dependency

- **NimBLE-Arduino** — install via the Arduino IDE Library Manager (Tools → Manage Libraries
  → search "NimBLE-Arduino"). Requires the **ESP32 board package** (Boards Manager → "esp32").

### Attribution note

Written without following a tutorial. The BLE plumbing uses the **NimBLE-Arduino** library in its
standard client pattern (scan → connect → subscribe); the ring-specific work — decoding its HID
report format and mapping gestures to drive commands — and the DRV8833 motor control are my own.
See the [reflection](../07_reflection/REFLECTION.md) for the full original-vs-adapted breakdown.
