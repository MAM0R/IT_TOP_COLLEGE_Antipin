#1

number = input("Введите число: ")

summa = 0 
count_digit = 0
count_zero = 0
middle = 0

for digit in number:
    summa += int(digit)
    count_digit += 1
    if digit == "0":
        count_zero += 1
middle = summa / count_digit

print(summa, count_digit, count_zero, middle)