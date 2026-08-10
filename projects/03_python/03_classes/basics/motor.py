class Motor:
    def __init__(self, name, temp):
        self.name = name
        self.temp = temp

    def heat_up(self, amount):
        self.temp += amount

    def cool_down(self, amount):
        self.temp -= amount

    def is_overheating(self):
        return self.temp > 70

    def __repr__(self):
        return f"Motor({self.name}, {self.temp}C)"


motor = Motor("arm", 55)
motor.heat_up(30)
print(motor)
print(motor.is_overheating())

motor.cool_down(20)
print(motor)
print(motor.is_overheating())
