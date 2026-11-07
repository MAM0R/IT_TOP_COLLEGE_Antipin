#3

import random

difficulty = int(input("Выберите уровень сложности (1 - легко, 2 - нормальный, 3 - сложно): "))
score = 0

if difficulty == 1:
    max_num = 5
    questions = 3
elif difficulty == 2:
    max_num = 8
    questions = 5
elif difficulty == 3:
    max_num = 10
    questions = 7
else:
    print("Неверный выбор сложности")

if max_num < 0 and questions < 0:
    for i in range(questions):
        a = random.randint (1, max_num)
        b = random.randint (1, max_num)
        ans = int(input(a,"*",b))
        if ans == a * b:
            score += 1

print("Правильных ответов:", score, "из", questions)