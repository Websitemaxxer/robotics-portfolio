import json

drone = {"id": "D7",
         "altitude": 120,
         "armed": False,
         "rotors": ["fl", "fr", "bl", "br"]}

text = json.dumps(drone)
print(text)
print(type(text))

back = json.loads(text)
print(f"Altitude + 30: {back['altitude'] + 30}")
print(f"Rotors: {len(back['rotors'])}")
