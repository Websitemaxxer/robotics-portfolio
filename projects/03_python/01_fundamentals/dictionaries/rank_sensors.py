signal = {"gps": 72, "lidar": 95, "camera": 60, "imu": 88, "sonar": 45}

ranked = sorted(signal.items(), key=lambda pair: pair[1], reverse=True)

for name, strength in ranked:
    print(f"{name}: {strength}%")

strongest = max(signal, key=signal.get)
weakest = min(signal, key=signal.get)

print(f"Strongest: {strongest}")
print(f"Weakest: {weakest}")
