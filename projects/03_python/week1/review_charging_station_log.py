# Week 1 review: charging station log — accumulator-pattern drill (attempt 2)
# Combines: grouping dict (list values), counting dict, set dedupe,
#           tuple unpacking, two-branch if/else, max() with key/lambda,
#           empty-data guard.
# Jul 25, 2026 — model code, verified with a full log and an empty log.
#
# Fixed four bugs from the first attempt:
#   1. grouping stored a running total (a number) instead of a list, so
#      sum()/len() in the summary raised "'int' object is not iterable".
#   2. the "most minutes" line sat inside the loop and used .values(), so
#      it lost the station name (the pairing problem).
#   3. the "most sessions" loop reset its best-so-far to 0 every pass and
#      printed every robot as the winner; replaced with one max()+unpack.
#   4. the empty-log guard was written len(log == 0) [len of a bool -> crash]
#      and placed at the bottom, after the code it was meant to protect.

log = [("dock_a", "scout", 72),
       ("dock_b", "rover", 30),
       ("dock_a", "rover", 55),
       ("dock_c", "digger", 40),
       ("dock_b", "scout", 65),
       ("dock_a", "digger", 50),
       ("dock_c", "rover", 20),
       ("dock_b", "scout", 35),
       ("dock_a", "scout", 44),
       ("dock_c", "digger", 25)
]

minutes_by_station = {}
sessions_per_robot = {}
over_60 = set()

for station, robot, minutes in log:
    if station in minutes_by_station:
        minutes_by_station[station].append(minutes)
    else:
        minutes_by_station[station] = [minutes]

    if robot in sessions_per_robot:
        sessions_per_robot[robot] += 1
    else:
        sessions_per_robot[robot] = 1

    if minutes > 60:
        over_60.add(station)

if len(log) == 0:
    print("The log is empty sorry!")
else:
    totals = []

    for station, minutes in minutes_by_station.items():
        total = sum(minutes)
        average = total / len(minutes)
        totals.append((station, total))

        if average > 45:
            status = "BUSY"
        else:
            status = "quiet"

        print(f"{station}: total {total} min, average {round(average, 1)} min - {status}")

    top_robot, top_count = max(sessions_per_robot.items(), key=lambda pair: pair[1])
    print(f"Most sessions: {top_robot} with {top_count}")

    over_60_list = ", ".join(sorted(over_60))
    print(f"Stations with a 60+ min session: {over_60_list}")

    busiest_station, busiest_total = max(totals, key=lambda pair: pair[1])
    print(f"Most total minutes: {busiest_station} with {busiest_total}")
