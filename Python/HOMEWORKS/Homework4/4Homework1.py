#1
num1 = int(input("Введите начало диапазона: "))
num2 = int(input("Введите конец диапазона: "))

if num1 > num2:
    print("Неправильно задан диапазон")

for i in range(num1, num2 + 1):
    if i % 7 == 0:
        print("Числа кратные 7:", i)
