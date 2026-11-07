#1
num1 = int(input("Введите первое число (должно быть больше 2-ого числа): "))
num2 = int(input("Введите второе число (должно быть меньше 1-ого числа): "))

sum_even = 0 
sum_odd = 0
sum_multi9 = 0

count_even = 0
count_odd = 0
count_multi9 = 0

if num1 > num2:
    print("Неверно задан диапазон")

for i in range (num1, num2 + 1):
    if i % 2 == 0:
        sum_even += i
        count_even += 1
    else:
        sum_odd += i
        count_odd += 1
    if i % 9 == 0:
        sum_multi9 += i
        count_multi9 += 1

print("Сумма чётных:", sum_even, "Среднее арф.:", sum_even / count_even)
print("Сумма нечётных:", sum_odd, "Среднее арф.:", sum_odd / count_odd)
print("Сумма кратных 9:", sum_multi9, "Среднее арф.:", sum_multi9 / count_multi9)