class Drone:
    def __init__(self, name, altitude):
        self.name = name
        self.altitude = altitude

    def is_airborne(self):
        return self.altitude > 0

    def __repr__(self):
        return f"Drone({self.name}, {self.altitude}m)"


class Fleet:
    def __init__(self):
        self.drones = []

    def add_drone(self, drone):
        self.drones.append(drone)

    def airborne_count(self):
        return len([drone for drone in self.drones if drone.is_airborne()])

    def highest(self):
        highest_drone = max(self.drones, key=lambda drone: drone.altitude)
        return highest_drone.name


fleet = Fleet()
fleet.add_drone(Drone("alpha", 120))
fleet.add_drone(Drone("bravo", 0))
fleet.add_drone(Drone("charlie", 85))
fleet.add_drone(Drone("delta", 200))

print(fleet.airborne_count())
print(fleet.highest())
