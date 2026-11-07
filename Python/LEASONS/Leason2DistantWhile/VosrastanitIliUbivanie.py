#2
#Дано два целых числа: a и b. Если a<b, то напечатайте числа от a до b в порядке возрастания. В противном случае, напечатайте числа от a до b в порядке убывания.


import random
a = random.randint(0, 20) #генерирует рандомное число от 0 до 20
b = random.randint(0, 20)

if a < b:
    while a <= b:
        print(a)
        a += 1
elif a > b:
    while a >= b:
        print(a)
        a -= 1
else:
    print("Числа равны")