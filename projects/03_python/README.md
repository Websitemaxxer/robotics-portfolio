# 03: Python

Python for robotics: sensor data handling, telemetry logging, configuration, and control logic. Organised into six topic areas, each split into subtopics with runnable, self-contained programs.

Runs on Python 3.13, standard library only (no external packages required).

## Topic areas

| Area | Covers | Status |
|------|--------|--------|
| [01_fundamentals](01_fundamentals/) | lists, dictionaries, tuples & sets, conditionals & loops, comprehensions, functions, data processing | Populated |
| [02_files_and_structure](02_files_and_structure/) | file I/O, exceptions, CSV, JSON, modules | Populated |
| [03_classes](03_classes/) | classes, methods, `__repr__`, composition | Populated |
| [04_numpy_and_plotting](04_numpy_and_plotting/) | arrays, masks, vectorised ops, Matplotlib | Planned |
| [05_hardware_control](05_hardware_control/) | pyserial, parsing serial data, Arduino commands, state machines | Planned |
| [06_projects](06_projects/) | original end-to-end builds combining earlier topics | Planned |

## 01: Fundamentals

**lists**, [sensor_readings.py](01_fundamentals/lists/sensor_readings.py) (flag proximity readings, count blocked, find the closest) · [moving_average.py](01_fundamentals/lists/moving_average.py) (rolling average over a sliding window with slicing) · [sort_readings.py](01_fundamentals/lists/sort_readings.py) (rank pairs with `sorted(key=lambda)`, take the top few)

**dictionaries**, [motor_temps.py](01_fundamentals/dictionaries/motor_temps.py) (overheating status, hottest motor, average) · [inventory.py](01_fundamentals/dictionaries/inventory.py) (tally parts with `.get`, sort, find the most used) · [rank_sensors.py](01_fundamentals/dictionaries/rank_sensors.py) (rank signal strengths with `sorted(items, key=lambda)`, strongest/weakest with `max`/`min` and `key`)

**tuples & sets**, [geometry_and_ids.py](01_fundamentals/tuples_and_sets/geometry_and_ids.py) (unpack coordinates, compute distances, dedupe sensor IDs with a set) · [set_membership.py](01_fundamentals/tuples_and_sets/set_membership.py) (use a set for fast membership checks, which required sensors are online)

**conditionals & loops**, [control_flow.py](01_fundamentals/conditionals_and_loops/control_flow.py) (a while countdown and a for scan using `break` and `continue`) · [state_machine.py](01_fundamentals/conditionals_and_loops/state_machine.py) (drive states idle → moving → paused with compound conditions)

**comprehensions**, [filter_readings.py](01_fundamentals/comprehensions/filter_readings.py) (filter and transform readings in one line) · [transform_readings.py](01_fundamentals/comprehensions/transform_readings.py) (several list comprehensions filtering and transforming the same readings)

**functions**, [pipeline.py](01_fundamentals/functions/pipeline.py) (a default argument, and a function returning several values that get unpacked) · [guards.py](01_fundamentals/functions/guards.py) (default and keyword arguments, one function feeding into another)

**data processing**, [telemetry_log.py](01_fundamentals/data_processing/telemetry_log.py) (group drone telemetry, count per zone, rank by average) · [fault_report.py](01_fundamentals/data_processing/fault_report.py) (count fault codes, group severities per robot, flag serious faults with a set) · [sensor_summary.py](01_fundamentals/data_processing/sensor_summary.py) (group readings by type, then rank the groups with `sort(key=lambda)`)

## 02: Files & structure

**file I/O**, [status_log.py](02_files_and_structure/file_io/status_log.py) (write status messages and read them back) · [log_analysis.py](02_files_and_structure/file_io/log_analysis.py) (write a log, then read and count error lines)

**exceptions**, [safe_config.py](02_files_and_structure/exceptions/safe_config.py) (handle a missing file) · [speed_guard.py](02_files_and_structure/exceptions/speed_guard.py) (raise a custom error for out-of-range speeds) · [parse_readings.py](02_files_and_structure/exceptions/parse_readings.py) (skip unparseable readings, average the rest)

**CSV**, [sensor_stats.py](02_files_and_structure/csv/sensor_stats.py) (read, summarise, write a summary CSV) · [components_dictreader.py](02_files_and_structure/csv/components_dictreader.py) (read rows by column name with DictReader) · [filter_csv.py](02_files_and_structure/csv/filter_csv.py) (read one CSV and write the matching rows to another) · [skip_bad_rows.py](02_files_and_structure/csv/skip_bad_rows.py) (skip invalid rows with try/except, then summarise the valid ones)

**JSON**, [robot_config.py](02_files_and_structure/json/robot_config.py) (save/load a config with types intact) · [telemetry_string.py](02_files_and_structure/json/telemetry_string.py) (convert to and from a JSON string) · [save_load_records.py](02_files_and_structure/json/save_load_records.py) (save a list of records, load and filter them)

**modules**, [robotics.py](02_files_and_structure/modules/robotics.py) + [main.py](02_files_and_structure/modules/main.py) (helpers imported into another file) · [telemetry.py](02_files_and_structure/modules/telemetry.py) + [analyse.py](02_files_and_structure/modules/analyse.py) (a second helper module used by an analysis script)

## 03: Classes

**basics**, [reading_log.py](03_classes/basics/reading_log.py) (a class with a name, an accumulating list of readings, methods to add a reading and return the average, and `__repr__`)

## Running

Each program is standalone:

```
cd 01_fundamentals/lists
python3 sensor_readings.py
```

Programs that read a data file create it first, so every file runs on its own with no setup.

## Environment

Developed inside a virtual environment (`python3 -m venv venv`, then `source venv/bin/activate`). All programs use only the Python standard library, so nothing needs installing to run them.
