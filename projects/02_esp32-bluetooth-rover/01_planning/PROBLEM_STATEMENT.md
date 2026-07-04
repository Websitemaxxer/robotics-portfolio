# Problem Statement — ESP32 Bluetooth Rover

> Written up after the fact from what the build actually was. It still serves its purpose:
> the success criteria below are the bar I can honestly check the finished rover against.

## Intended user / purpose

> For me, to learn. This was a personal hobby project. I wanted a hands-on way to understand
> three things that keep coming up in robotics — **Bluetooth Low Energy (BLE)**, **H-bridge
> motor driving**, and **PWM** — by building something I could actually drive around, rather
> than just reading about them.

## The problem

> Build a small tracked rover that can be **driven wirelessly** in all four directions
> (forward, backward, left, right) from a **wearable Bluetooth ring**, using an ESP32 as the
> brain and a proper motor driver so the ESP32 never drives the motors directly.

## Measurable success criteria

- Rover drives **forward, backward, left, and right** on command. ✅
- Control is **wireless** via the Bluetooth ring, usable across a room. ✅
- Two motors are driven through an **H-bridge**, with **PWM** setting speed/direction (ESP32
  pins never wired straight to a motor). ✅
- Connection is **robust**: if the ring disconnects or scanning stalls, the rover reconnects
  on its own without a power cycle. ✅
- Keep it **cheap** (hobby budget). ✅ (~150 AED total)

## Constraints

- **Budget:** hobby-level; came in around **150 AED** total.
- **Parts on hand:** ESP32 dev board, DRV8833 driver module, 2× N20 gear motors, LEGO Technic
  tracks/sprockets, a laser-cut acrylic base, a 9V battery, and an off-the-shelf Bluetooth ring.
- **Skills to learn during the build:** BLE client/HID on ESP32, decoding raw HID reports,
  H-bridge control, and PWM.
- **Power:** a single 9V battery has to run both the motors and the ESP32.

## System diagram

Power (9V) → on/off switch → DRV8833 motor supply **and** ESP32.
ESP32 ⇄ **Bluetooth ring** (BLE HID, receives gestures) → ESP32 sets 4 PWM pins + enable →
DRV8833 → 2 motors → LEGO Technic tracks.

> A cleaner diagram would help here. Options:
> - Export the Fritzing circuit ([`../03_electronics/rover_circuit.fzz`](../03_electronics/rover_circuit.fzz))
>   to an image, **or**
> - draw the power→controller→driver→motors flow on paper and photograph it,
>
> then save it to `../05_media/photos/system_diagram.png` and link it here.
