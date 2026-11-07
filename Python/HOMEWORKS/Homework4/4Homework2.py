#2
num1 = int(input("Введите начало диапазона: "))
num2 = int(input("Введите конец диапазона: "))
count_5 = 0

if num1 > num2:
    print("Неправильно задан диапазон")

#1. Все числа диапазона:
print("Все числа диапазона:")
for i in range(num1, num2 + 1):
    print(i, end = ",")

#2. Все числа диапазона в убывающем порядке:
print("\nЧисла диапазона в убывающем порядке:")
for i in range (num2, num1 - 1, -1):
    print(i, end = ",")

#3. Все числа, кратные 7:
print("\nЧисла кратные 7:")
for i in range(num1, num2 + 1):
    if i % 7 == 0:
        print(i, end = ",")

#4. Количество чисел, кратных 5:
print("\nКол-во чисел кратных 5:")
for i in range(num1, num2 + 1):
    if i % 5 == 0:
        count_5 += 1
print(count_5)

