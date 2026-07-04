# Wiring — ESP32 Bluetooth Rover

## Circuit

The circuit was designed in Fritzing: [`rover_circuit.fzz`](rover_circuit.fzz).

> To show it in the portfolio, open the `.fzz` in Fritzing and export the breadboard/schematic
> view as an image to `../05_media/photos/wiring_diagram.png`, then it will appear here:
>
> <!-- ![Wiring diagram](../05_media/photos/wiring_diagram.png) -->

## Pin map

An **ESP32 WROOM DevKit** drives a **DRV8833** dual H-bridge module (silkscreen "HW-627"),
which powers the two drive motors. The pin numbers below match both the firmware
(`04_code/02_rover_ble_ring/`) **and** the labels printed on the DRV8833 module itself.

| ESP32 pin | DRV8833 module label | Function |
|-----------|----------------------|----------|
| GPIO 27 | `EEP` | Driver enable (DRV8833 `nSLEEP`) — HIGH = awake, LOW = sleep/coast |
| GPIO 25 | `IN3` (Motor A) | Motor A input 1 (PWM) → `A OUT1` |
| GPIO 26 | `IN4` (Motor A) | Motor A input 2 (PWM) → `A OUT2` |
| GPIO 16 | `IN1` (Motor B) | Motor B input 1 (PWM) → `B OUT1` |
| GPIO 17 | `IN2` (Motor B) | Motor B input 2 (PWM) → `B OUT2` |
| GPIO 2  | Onboard LED | Status — lit while the ring is connected |

Each motor drives one LEGO Technic track (tank / differential steering). `A OUT1/2` and
`B OUT1/2` go to the two N20 micro gear motors.

**Direction & speed (H-bridge + PWM):** each motor has two inputs. Driving one input with a
PWM value and holding the other at 0 spins the motor one way; swapping them reverses it. The
PWM duty (0–255 via `analogWrite`) sets the speed. Turning is done by driving the two tracks
in opposite directions.

> **Code quirk:** GPIO16/17 are labelled `rx pin` / `tx pin` in the source comments — leftover
> names from an earlier idea. They are used purely as Motor B's PWM inputs, not as a serial port.

## Power

- **Battery:** single **9V** battery (Energizer MAX), via the module's `9V Power+` screw terminal.
- **Motor supply:** 9V feeds the DRV8833 motor voltage (`VM`).
- **Controller supply:** the ESP32 is powered from the same pack (through its onboard regulator).
- **On/off:** a slide switch on the driver board cuts power to the whole rover.
- **Common ground:** ESP32 GND ↔ DRV8833 GND ↔ battery − are all tied together.
- **Measured current draw:** not measured.

## Gotchas / notes

- The DRV8833 must be woken up (`EEP` / `nSLEEP` HIGH) before any motor command does anything —
  the bring-up sketch confirmed this before the BLE code was added.
- A 9V alkaline has limited current, so a higher-current pack would be the safer choice for a
  motor load — worth keeping in mind if the ESP32 ever browns out under heavy driving.
