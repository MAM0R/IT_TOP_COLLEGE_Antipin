#8
score = int(input("Введите кол-во баллов (0-100): "))

if score >= 90 and score <= 100:
    print("Оценка: Отлично")
    
if score >= 75 and score <= 89:
    print("Оценка: Хорошо")
    
if score >= 60 and score <=74:
    print("Оценка: Удовлетворительно")

if score >= 0 and score <= 59:
    print("Оценка: Неудовлетворительно")

if score < 0:
    print("Неверный ввод")

if score > 100:
    print("Неверный ввод")