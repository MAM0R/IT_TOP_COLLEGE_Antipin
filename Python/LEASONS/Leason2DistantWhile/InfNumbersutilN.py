#3
#Человек вводит неограниченное количество чисел, пока он не написал букву “N”. Посчитайте их среднее арифметическое. 

amount = 0
count = 0
while True: #бесконечный цикл
    symbol = input("Введите число")
    
    if symbol == "N":
        break #прерывает цикл
    
    if not symbol.isdigit(): # если symbol не состоит из цифр, например пробел
        continue # пропуск итерации
    
    amount += int(symbol)
    count += 1

print("Среднее арифметическое:", amount / count)