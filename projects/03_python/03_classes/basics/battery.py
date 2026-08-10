class Battery:
    def __init__(self, name, charge):
        self.name = name
        self.charge = charge

    def drain(self, amount):
        self.charge -= amount

    def recharge(self, amount):
        self.charge += amount

    def is_low(self):
        return self.charge < 20

    def __repr__(self):
        return f"Battery({self.name}, {self.charge}%)"


battery = Battery("main", 100)
battery.drain(85)
print(battery)
print(battery.is_low())

battery.recharge(50)
print(battery)
print(battery.is_low())
