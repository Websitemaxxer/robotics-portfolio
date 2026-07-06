# Problem Statement — Arduino Starter Kit

Write this **before** you start building. It keeps the project honest: at the end
you can check whether you actually hit the success criteria you set here.

## Intended user / purpose

For me — to build a genuine, hands-on foundation in electronics and embedded programming
that later projects (rovers, robot arms, sensor systems) will stand on. I'd rather learn
the fundamentals properly on a known-good kit than fake my way through them.

## The problem

I can follow high-level robotics tutorials but I don't yet have the underlying skills:
reading a wiring diagram, building a circuit on a breadboard, understanding pull-down
resistors and LED polarity, and writing/uploading C/C++ that reacts to inputs. This
project closes that gap by working through the kit's guided builds and then extending
selected ones myself.

## Measurable success criteria

- Complete the **15 guided projects** in the Arduino Starter Kit.
- Write **≥ 3 of my own extensions** (a behaviour change or added logic), clearly labelled as mine.
- Be comfortable enough with **≥ 3 sensors/components** to reuse them in a future project without the book.
- For each project: circuit behaves as intended, with **at least one documented failure + fix** where things went wrong.

## Constraints

- **Budget:** one Arduino Starter Kit (parts limited to what's in the box).
- **Tools:** no multimeter yet, so I diagnose with test sketches and the Serial Monitor rather than measurements.
- **Time:** fitting sessions around school; progress is project-by-project, not all at once.
- **Skills:** starting as a beginner at breadboarding and embedded C.

## System diagram

Each guided project has its own small circuit; the per-project wiring lives in
[`../03_electronics/WIRING.md`](../03_electronics/WIRING.md) with a photo/pin map.

Example — **Project 2 (Spaceship Interface):**

> USB 5 V → Arduino Uno → pushbutton input (D2) decides state → drives green LED (D3, idle)
> or two alternating red LEDs (D4/D5, alarm).
