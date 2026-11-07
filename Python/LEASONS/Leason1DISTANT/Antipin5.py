#5
number1 = int(input("Введите первое число: "))
number2 = int(input("Введите второе число: "))
operation = input("Введите операцию (+, -, *, /): ")

if operation == "+":
    print("Ответ:", number1 + number2)
    
if operation == "-":
    print("Ответ:", number1 - number2)
    
if operation == "*":
    print("Ответ:", number1 * number2)
    
if operation == "/" and number2 != 0:
    print("Ответ:", number1 / number2)

if operation == "/" and number2 == 0:
    print("Ошибка, деление на 0 не возможно")
    
else:
    print("Неверный ввод")
