# Code: ESP32 Bluetooth Rover

Two sketches, in the order they were written. Each folder is a self-contained Arduino sketch (the `.ino` matches its folder name).

> Sketches were renamed from their original `sketch_feb16a.ino` / `sketch_feb20a.ino` names when added; the code is unchanged.

## `01_motor_bringup_test/`: H-bridge + PWM bring-up

A no-Bluetooth test to prove the motor wiring and the DRV8833 H-bridge before adding wireless control.

- Enables the driver by pulling the DRV8833 `nSLEEP` pin (GPIO 27, labelled `eep` in code) HIGH.
- Defines `goForward()`, `goBackward()`, `goLeft()`, `goRight()`, `stopAll()`, each setting the four motor-input pins with `analogWrite()` (PWM). Direction on each motor is set by which of its two inputs is driven and which is held at 0; speed is the PWM value (0-255).
- `loop()` cycles forward → stop → backward on a short delay to confirm both motors spin both ways.

H-bridge idea: two inputs per motor, and swapping which one is high reverses the current, reversing the spin.

## `02_rover_ble_ring/`: full rover firmware (BLE ring control)

The complete firmware, using NimBLE-Arduino to talk to a Bluetooth smart ring and turn its gestures into driving commands.

1. **Scan & match:** scans for BLE devices advertising the HID service (`0x1812`) and matches the ring by its MAC address (`targetAddrStr`).
2. **Connect & subscribe:** connects as a BLE client, finds the HID Report characteristic (`0x2A4D`), and subscribes to its notifications.
3. **Decode gestures (`notifyCB`):** parses each 8-byte HID report (an active flag, a gesture group id, and signed 16-bit X/Y), and on finger-release compares first vs last X/Y:
   - horizontal swipe → `LEFT` / `RIGHT`
   - vertical swipe → `FORWARD` / `BACKWARD`
   - tap / specific group → `STOP`
4. **Drive:** `loop()` maps the current command to the H-bridge motor functions from the bring-up sketch (tank steering: turning drives the two sides in opposite directions), re-issuing motor writes only when the command changes, and lights the onboard LED (GPIO 2) while connected.
5. **Self-healing BLE:** a watchdog restarts scanning and fully re-initialises the BLE stack if the connection drops or scanning stalls.

### Library dependency

- **NimBLE-Arduino**, install via the Arduino IDE Library Manager (Tools → Manage Libraries → search "NimBLE-Arduino"). Requires the **ESP32 board package** (Boards Manager → "esp32").

### Attribution

Written without a tutorial. The BLE plumbing uses NimBLE-Arduino in its standard client pattern (scan → connect → subscribe); the ring HID decoding and the DRV8833 motor control are my own.
