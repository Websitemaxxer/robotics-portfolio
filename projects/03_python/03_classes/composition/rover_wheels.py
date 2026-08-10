class Wheel:
    def __init__(self, name, wear_level):
        self.name = name
        self.wear_level = wear_level

    def needs_replacing(self):
        return self.wear_level > 80

    def __repr__(self):
        return f"Wheel({self.name}, {self.wear_level}%)"


class Rover:
    def __init__(self):
        self.wheels = []

    def add_wheel(self, wheel):
        self.wheels.append(wheel)

    def wheel_replacements(self):
        return [wheel.name for wheel in self.wheels if wheel.needs_replacing()]


rover = Rover()
rover.add_wheel(Wheel("front_left", 20))
rover.add_wheel(Wheel("front_right", 90))
rover.add_wheel(Wheel("back_right", 10))
rover.add_wheel(Wheel("back_left", 49))

print(rover.wheel_replacements())
