#9
age = int(input("Введите Ваш возраст: "))
day_of_the_week = int(input("Введите день недели (число дня недели): "))
base_price = 500
percent = 0
final_price = 0

if age <= 12:
    percent -= 50

if age >= 65:
    percent -= 30

if day_of_the_week == 6 or day_of_the_week == 7:
    percent += 20

final_price = base_price + (base_price * percent / 100)
print("Итоговая цена билета:", final_price, "руб")
