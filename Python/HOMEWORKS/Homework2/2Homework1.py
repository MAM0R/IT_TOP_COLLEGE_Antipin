#1

num1 = int(input("Введите 1-ое число: "))
num2 = int(input("Введите 2-ое число: "))
num3 = int(input("Введите 3-ое число: "))

choice = input("Выберитье из двух вариантов: сумма или произведение: ")

if choice == "сумма":
    print("Сумма этих чисел:", num1 + num2 + num3)
    
elif choice == "произведение":
    print("Произведение этих чисел:", num1 * num2 * num3)

else:
    print("Неверный ввод")


        
