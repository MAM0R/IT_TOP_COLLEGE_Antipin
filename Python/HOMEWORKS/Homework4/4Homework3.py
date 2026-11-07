#3
num1 = int(input("Введите начало диапазона: "))
num2 = int(input("Введите конец диапазона: "))
count_5 = 0

if num1 > num2:
    print("Неправильно задан диапазон")

for i in range(num1, num2 + 1):
    if i % 3 == 0 and i % 5 == 0:
        print("Fizz Buzz")
    elif i % 3:
        print("Fizz")
    elif i % 5 == 0:
        print("Buzz")
    else:
        print(i)