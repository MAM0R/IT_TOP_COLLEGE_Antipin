#2

board = int(input("Введите размер клеточки: "))

for i in range (8):
    for j in range(board):
        if i % 2 == 0:
            print(("*" * board + "-" * board) * 4)
        else:
            print(("-" * board + "*" * board) * 4)