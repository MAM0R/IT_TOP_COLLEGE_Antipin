#2

import random

numbers = []
for i in range(10):
    numbers.append(random.randint(-10,10))

print("Все числа:", numbers)

even = []
not_even = []
neg = []
pos = []

for a in numbers:
    if a % 2 == 0:
        even.append(a)
    else:
        not_even.append(a)
    if a < 0:
        neg.append(a)
    elif a > 0:
        pos.append(a)

print("Чётные:", even, "\n Нечётные:", not_even)
print("Отрицательные:", neg, "\n Положительные:", pos)