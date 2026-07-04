# Test Log — ESP32 Bluetooth Rover

Each test records what was verified. The rover is finished and working; the tests below capture
the functional results. I didn't take quantitative measurements at the time — that gap is noted
honestly at the bottom rather than left implied.

---

## Test 1 — Motor / H-bridge bring-up — 2026-02-16

- **Setup:** ESP32 + DRV8833 wired up, `01_motor_bringup_test` sketch, powered but rover on a
  stand so the tracks can spin freely.
- **Procedure:** upload the sketch; it enables the driver (`EEP` HIGH) and cycles each motor
  forward → stop → backward.
- **Result:** both motors spun in both directions; nothing responded until the `EEP` enable
  pin was HIGH.
- **Pass / fail vs target:** target = both motors driveable via H-bridge + PWM → **PASS**.
- **What I'd change:** if I revisit it, check the two motors run at matched speed so the rover
  tracks straight.

---

## Test 2 — Bluetooth ring connect & gesture decode — 2026-02-20

- **Setup:** `02_rover_ble_ring` firmware, ring powered on, ESP32 running with Serial monitor open.
- **Procedure:** power on; watch the Serial log find the ring by MAC, connect, and subscribe;
  then swipe/tap the ring and read the printed `CLICK:` command values.
- **Result:** ring found and subscribed; gestures printed the expected FORWARD/BACKWARD/LEFT/
  RIGHT/STOP commands.
- **Pass / fail vs target:** target = ring gestures reliably decoded → **PASS**.
- **What I'd change:** the mapping is tied to this specific ring's report format; a cleaner
  version would decode the gestures less rigidly.

---

## Test 3 — Full driving test — 2026-02-23

- **Setup:** fully assembled rover on the floor, 9V battery, driven by the ring.
- **Procedure:** drive forward/back/left/right; deliberately move out of range / power-cycle
  the ring to check the rover reconnects on its own.
- **Result:** drove in all four directions; watchdog re-scanned and re-connected after drops.
- **Pass / fail vs target:** target = drive all directions + self-reconnect → **PASS**.
- **What I'd change:** add proportional speed control (swipe distance → PWM) instead of fixed
  full-speed moves.

---

## Measurements not taken

I verified the rover functionally (all four directions + self-reconnect above) but didn't take
quantitative measurements at the time. If I revisit the rover, the numbers worth capturing are:
top speed (m/s over a measured distance), wireless range (m), current draw (mA, idle vs driving),
and battery life on one 9V. Noting this as an honest gap rather than leaving it implied.
