import time

n = int(input())

while n > 0:
    print(f"Осталось секунд: {n}")
    time.sleep(1)
    n -= 1
print("Пуск")
