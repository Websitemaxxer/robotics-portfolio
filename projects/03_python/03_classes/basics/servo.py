class Servo:
    def __init__(self, name, angle):
        self.name = name
        self.angle = angle

    def rotate_to(self, target):
        if target < 0:
            self.angle = 0
        elif target > 180:
            self.angle = 180
        else:
            self.angle = target

    def __repr__(self):
        return f"Servo({self.name}, {self.angle} degrees)"


servo = Servo("gripper", 90)

servo.rotate_to(200)
print(servo)

servo.rotate_to(-30)
print(servo)

servo.rotate_to(45)
print(servo)
