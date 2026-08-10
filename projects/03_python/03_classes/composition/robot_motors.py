class Motor:
    def __init__(self, name, temp):
        self.name = name
        self.temp = temp

    def is_overheating(self):
        return self.temp > 70

    def __repr__(self):
        return f"Motor({self.name}, {self.temp}C)"


class Robot:
    def __init__(self, name):
        self.name = name
        self.motors = []

    def add_motor(self, motor):
        self.motors.append(motor)

    def overheating_count(self):
        return len([motor for motor in self.motors if motor.is_overheating()])

    def hottest(self):
        hottest_motor = max(self.motors, key=lambda motor: motor.temp)
        return hottest_motor.name


robot = Robot("scout")
robot.add_motor(Motor("left", 55))
robot.add_motor(Motor("right", 82))
robot.add_motor(Motor("arm", 91))
robot.add_motor(Motor("base", 40))

print(robot.overheating_count())
print(robot.hottest())
