# Reflection — ESP32 Bluetooth Rover

- **What was original?** What did I design, write, or figure out myself?
  > The whole rover concept and assembly: the tracked chassis (LEGO Technic tracks/sprockets on
  > a laser-cut acrylic base, two N20 motors for tank steering), the ESP32 → DRV8833 wiring, and
  > all of the motor-control code — the `goForward/Backward/Left/Right/stop` functions using PWM
  > and the `EEP` enable pin. On the software side, the logic that turns the ring's raw HID
  > reports into drive commands (the swipe/tap → direction mapping) and the reconnect watchdog
  > are mine.

- **What was adapted, and from where?** Kits, tutorials, open-source designs, code snippets —
  name them and link them.
  > The main external dependency is the **NimBLE-Arduino** library — the firmware's BLE-client
  > structure (callbacks → scan → connect → subscribe) follows that library's standard usage
  > pattern, which is just how you drive it. I didn't follow a tutorial for the ring connection; I
  > worked it out myself. The one thing I clearly didn't make is the ring: it's an off-the-shelf
  > Bluetooth remote, and I only decoded the HID reports it sends rather than writing its firmware.

- **Hardest problem + how I solved it.** The one that nearly stopped me.
  > Getting a **reliable Bluetooth connection** to the ring. The raw link would stall or drop, so I
  > solved it with a two-level **watchdog** in `loop()`: if scanning stalls it restarts the scan,
  > and if nothing comes back for several seconds it fully re-initialises the BLE stack — plus the
  > firmware clears all bonds on boot to avoid stale pairing state. That recovery logic is what
  > lets the rover recover on its own instead of needing a reset. Alongside that, decoding the
  > ring's HID reports (which bytes are X/Y, which "click group" is which gesture) took real trial
  > and error.

- **What I'd do differently next time.**
  > Use a **higher-current battery** than a 9V alkaline
  > so the motors can't brown out the ESP32; clean up the leftover `rx/tx` pin names in the code;
  > and add real **speed control** (right now movement is basically full-on PWM rather than
  > proportional to how far you swipe).

- **What transfers to the next project?** Skills, tools, or habits I'll reuse.
  > BLE client + HID handling on the ESP32, driving motors through an H-bridge with PWM,
  > structuring firmware as clean reusable functions, and using a watchdog/self-reset pattern to
  > make a wireless link robust. These carry straight into any future ESP32 or robot-control build.

- **What skills does this project prove?**
  > Writing & uploading embedded C/C++ to a microcontroller; driving motors from code via an
  > H-bridge + PWM; debugging over serial; wireless (BLE) communication and decoding a HID
  > protocol; assembling a working tracked drivetrain; powering a project safely; and building a
  > CAD (Blender) model of the design. (Matching boxes are ticked in the top-level `README.md`.)
