#1
number = int(input("Введите число: "))

if number > 0:
    print("Число положительное")
elif number < 0:
    print("Число отрицательное")
elif number == 0:
    print("Число равно нулю")
else:
    print("Неверный ввод")