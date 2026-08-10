class Sensor:
    def __init__(self, name, value):
        self.name = name
        self.value = value

    def is_faulty(self):
        return self.value < 5

    def __repr__(self):
        return f"Sensor({self.name}, {self.value})"


class Rover:
    def __init__(self, name):
        self.name = name
        self.sensors = []

    def add_sensor(self, sensor):
        self.sensors.append(sensor)

    def faulty_names(self):
        return [sensor.name for sensor in self.sensors if sensor.is_faulty()]

    def average_value(self):
        values = [sensor.value for sensor in self.sensors]
        return round(sum(values) / len(values), 1)

    def __repr__(self):
        return f"Rover({self.name}, {len(self.sensors)} sensors)"


rover = Rover("rover")
rover.add_sensor(Sensor("electrical", 84))
rover.add_sensor(Sensor("nuclear", 2))
rover.add_sensor(Sensor("mechanical", 12))
rover.add_sensor(Sensor("kinetic", 54))

print(rover.faulty_names())
print(rover.average_value())
print(rover)
