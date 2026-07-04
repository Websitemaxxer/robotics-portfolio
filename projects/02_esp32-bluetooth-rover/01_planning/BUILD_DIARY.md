# Build Diary — ESP32 Bluetooth Rover

**This is the most valuable file in the project.** Newest entry at the **TOP**.

> **Note:** I built this rover in **February 2026** and logged it into the portfolio a few months
> later, so these entries are **reconstructed from my own files** — the two dated sketches (Feb 16
> and Feb 20), the DRV8833 wiring, and the firmware itself. Where the day-to-day details had
> faded, I've described the problems and fixes that the **code actually shows** (for example the
> reconnect watchdog), so everything below is accurate even if some moment-to-moment memories
> aren't sharp anymore.

---

## 2026-02-23 — Final assembly, tidy-up, and driving it

- **Time spent:** about 4 hours
- **Goal today:** get everything mounted on the chassis and actually drive the rover.
- **What I did:** finished mounting the ESP32 + DRV8833 on the acrylic base, ran the motor
  wires to the driver's `A OUT`/`B OUT` terminals, fitted the 9V battery underneath, and drove
  the rover around using the ring. Also made a Blender model of the rover
  ([`../02_cad/rover_model.blend`](../02_cad/rover_model.blend)) and put together a short
  presentation ([`../05_media/rover_project_presentation.odp`](../05_media/rover_project_presentation.odp)).
- **What worked:** all four directions drove correctly from the ring; the tank-style turning
  (tracks driven in opposite directions) worked.
- **What failed / surprised me:** nothing major on the mechanical side — the tracked chassis and
  motor mounting held together and drove cleanly. All the fiddly problems on this project were on
  the software/Bluetooth side (see the Feb 20 entry), not the build.
- **What I changed because of it:** nothing needed changing this session — it was assembly and
  wiring, not debugging.
- **Next step:** log it into the portfolio (done now).

---

## 2026-02-20 — Bluetooth ring: pairing and decoding the gestures

- **Time spent:** about 5 hours
- **Goal today:** get the ESP32 to connect to the Bluetooth ring and turn its input into
  drive commands.
- **What I did:** used the **NimBLE-Arduino** library to scan for the ring (it advertises as a
  BLE **HID** device, service `0x1812`), matched it by MAC address, connected as a client, and
  subscribed to its HID report characteristic (`0x2A4D`). Then wrote `notifyCB` to parse the
  raw 8-byte reports — a button/active flag plus signed X/Y values — and map a swipe/tap into
  `FORWARD / BACKWARD / LEFT / RIGHT / STOP`. Wired that into the motor functions from the
  bring-up sketch. Result: [`../04_code/02_rover_ble_ring/`](../04_code/02_rover_ble_ring/).
- **What worked:** once subscribed, the gestures came through and the rover responded.
- **What failed / surprised me:** getting a *stable* connection was the hard part. The evidence is
  baked into the firmware: it clears all Bluetooth bonds on every boot (`deleteAllBonds()`), and it
  carries a **watchdog** in `loop()` that restarts scanning and, if no results come back for
  several seconds, fully re-initialises the BLE stack (`resetBluetoothStack()`) — recovery logic
  you only write when the raw connection is stalling and dropping. Decoding the ring was non-trivial
  too: the code keys on specific "click groups" and X/Y deltas, the kind of magic numbers you only
  arrive at by watching what the ring actually sends.
- **What I changed because of it:** added the reconnect/reset watchdog, the bond-clearing on boot,
  and the `prevCommand` check so motor writes only fire when the command actually changes.
- **Next step:** mount everything and drive it (Feb 23).
- **How I built it:** I wrote this firmware myself without following a tutorial. It's built on the
  **NimBLE-Arduino** library and follows that library's standard BLE-client pattern (callbacks →
  scan → connect → subscribe); the ring-specific part — reverse-engineering its HID report format
  and mapping gestures to directions — I worked out by inspecting the reports the ring sends.

---

## 2026-02-16 — Motors + H-bridge bring-up (no Bluetooth yet)

- **Time spent:** about 3 hours
- **Goal today:** prove the motors, the DRV8833 H-bridge, and PWM before touching Bluetooth.
- **What I did:** wired the ESP32 to the DRV8833 (`IN1–IN4` on GPIO 25/26/16/17, enable `EEP`
  on GPIO 27) and wrote a no-Bluetooth test sketch that enables the driver and cycles the
  motors forward → stop → backward using `analogWrite` (PWM). Wrote `goForward/goBackward/
  goLeft/goRight/stopAll` as reusable functions. Code: [`../04_code/01_motor_bringup_test/`](../04_code/01_motor_bringup_test/).
- **What worked:** motors spun both directions once the `EEP`/enable pin was driven HIGH —
  confirmed the H-bridge and PWM approach before adding wireless.
- **What failed / surprised me:** the main gotcha with the DRV8833 is the **enable pin** — it does
  nothing at all until `EEP` (GPIO27) is HIGH, which is exactly why this sketch drives it HIGH in
  `driverOn()` before any movement. I built the test around explicit `driverOn()` / `driverOff()`
  helpers to keep that in control.
- **What I changed because of it:** in the later BLE version I simplified this — dropping the
  helpers and writing the enable pin directly inside each movement function.
- **Next step:** add Bluetooth ring control (Feb 20).
