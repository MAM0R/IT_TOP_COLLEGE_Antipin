#1

import random

numbers = []
for i in range(10):
    numbers.append(random.randint(-10,10))

print("Все числа:", numbers)

#Суммы отрицательных, четных и нечетных:
sum_neg = 0
sum_even = 0
sum_noteven = 0

for a in numbers:
    if a < 0:
        sum_neg += a
    elif a % 2 == 0:
        sum_even += a
    else:
        sum_noteven += a
print("Сумма отрицательных", sum_neg, "\n Сумма чётных:", sum_even, "\n Сумма нечётных:", sum_noteven)

#Произведение элементов с индексами кратными 3:
ind3 = 1
for i in range(len(numbers)):
    if i % 3 == 0:
        ind3 *= numbers[i]
print("Произведение с индексами кратными 3:", ind3)

#Произведение элементов между минимальным и максимальным
min_i = numbers.index(min(numbers))
max_i = numbers.index(max(numbers))

if min_i > max_i:
    start = max_i + 1
    finish = min_i
else:
    start = min_i + 1
    finish = max_i

prod5 = 1
for i in range(start, finish):
    prod5 *= numbers[i]
print("Произведение элементов между минимальным и максимальным", prod5)

#Сумма элементов между первым и последним положительным
first = -1
last = -1
sum_pos = 0

for i in range(len(numbers)):
    if numbers[i] > 0:
        if first == -1:
            first = i
        last = i

for i in range(first + 1, last):
    sum_pos += numbers[i]
print("Сумма элементов между первым и последним положительным:", sum_pos)