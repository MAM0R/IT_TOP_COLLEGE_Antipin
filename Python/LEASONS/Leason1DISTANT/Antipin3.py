#3
number1 = int(input("Введите первое число: "))
number2 = int(input("Введите второе число: "))

if number1 == number2:
    print("Два этих числа равны")
else:
    print("Наибольшее число:", max(number1,number2))