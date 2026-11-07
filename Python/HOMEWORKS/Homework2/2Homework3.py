#3

amount_meters = int(input("Введите количество метров: "))

choice = input("Выберите Во что нужно перевести метры: мили, дюймы, ярды: ")

if choice == "мили":
    print("Перевод в мили:", amount_meters / 1609.34)

elif choice == "дюймы":
    print("Перевод в дюймы:", amount_meters * 39.37)

elif choice == "ярды":
    print("Перевод в ярды:", amount_meters * 1.094)

else:
    print("Неверный ввод")
    
