sum: float = 0
counts: int = 0

while (True):
    temperature = float(input(f"tmp day_{counts + 1}: "))

    if (temperature <= -300):
        break
    sum += temperature

    counts += 1

if (counts == 0):
    print("enter at least one value")

else:
    print("average temperature =", sum / counts)
