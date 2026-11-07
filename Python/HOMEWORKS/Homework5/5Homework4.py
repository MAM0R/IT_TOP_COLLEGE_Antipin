#4
total = 0
max_num = 0
min_num = 0

while True:
    num = int(input("Введите число: "))
    
    if num == 7:
        print("Good bye!")
        break
    
    total_sum += num
    
    if num > max_num:
        max_num = num
    if num < min_num:
        min_num = num
    

print("Сумма:", total, "Максимум:", max_num, "Минимум:", min_num)