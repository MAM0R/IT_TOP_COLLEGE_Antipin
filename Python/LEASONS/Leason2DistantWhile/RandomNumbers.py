#1
#Дано два числа: a и b, a<b. Напечатать в строчку все числа от a до b включительно, а также квадраты этих чисел.

import random
a = random.randint(0, 20)
b = random.randint(20, 40)

while a <= b:
    print(a)
    a += 1