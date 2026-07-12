# Variables & types — completed Jul 12, 2026
# Create int/float/str/bool, check with type(), convert between types.

age = 15
iq = 15.4
name = "kush"
boy = True
reading = "42"  # a string, like data arriving over serial

print(type(age))
print(type(iq))
print(type(name))
print(type(boy))

print(int(iq))                       # -> 15 (int() chops, doesn't round)
print(f"{name} is {age} years old")  # f-string
result = int(reading) + 8            # string -> int before math
print(result)                        # -> 50
