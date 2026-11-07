#10
password = input("Введите пароль: ")

if len(password) < 8:
    print("Пароль должен быть длиной не менее 8 символов")

if len(password) >= 8:
    print("Пароль надёжный, поздравляем!")