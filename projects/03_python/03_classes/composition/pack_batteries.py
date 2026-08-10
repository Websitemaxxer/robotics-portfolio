class Battery:
    def __init__(self, name, charge):
        self.name = name
        self.charge = charge

    def is_low(self):
        return self.charge < 20

    def __repr__(self):
        return f"Battery({self.name}, {self.charge}%)"


class Pack:
    def __init__(self):
        self.batteries = []

    def add_battery(self, battery):
        self.batteries.append(battery)

    def low_names(self):
        return [battery.name for battery in self.batteries if battery.is_low()]

    def average_charge(self):
        charges = [battery.charge for battery in self.batteries]
        return round(sum(charges) / len(charges), 1)


pack = Pack()
pack.add_battery(Battery("cell_a", 18))
pack.add_battery(Battery("cell_b", 79))
pack.add_battery(Battery("cell_c", 12))
pack.add_battery(Battery("cell_d", 40))

print(pack.low_names())
print(pack.average_charge())
