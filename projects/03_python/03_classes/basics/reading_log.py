class Robot:
    def __init__(self, name):
        self.name = name
        self.readings = []

    def add_reading(self, reading):
        self.readings.append(reading)

    def average(self):
        return sum(self.readings) / len(self.readings)

    def __repr__(self):
        return f"Robot({self.name}, {len(self.readings)} readings)"


robot = Robot("scout")
robot.add_reading(90)
robot.add_reading(23)
robot.add_reading(85)

print(robot)
print(robot.average())
