import os

game_field = [["  ","  ","  "], ["  ","  ","  "], ["  ","  ","  "]]

def start_menu():
    print('''Х=О=Х=О=Х=О Игра Крестики-нолики Х=О=Х=О=Х=О
    для начала игры введите start
    для выхода введите exit
    для помощи введите help''')
    while True:
        menu = input(">")
        if str.lower(menu) == "start":
            print("начинаем")
            start_game()
            break
        elif str.lower(menu) == "exit":
            print("выходим")
            break
        elif str.lower(menu) == "help":
            print("помощь")
            help_page()
            break
        else:
            print("введена неверная команда, попробуйте еще раз")

def draw_field(field):
    """отрисовка игрового поля"""
    os.system('cls||clear')
    print(f'''  1 2 3
1{field[0][0]}{field[0][1]}{field[0][2]}
2{field[1][0]}{field[1][1]}{field[1][2]}
3{field[2][0]}{field[2][1]}{field[2][2]}
''')

def check_step(step):
    """проверка правильности введенных координат"""
    s = list(step)
    if len(s) != 2:
        return False
    if (s[0] == "1" or s[0] == "2" or s[0] == "3") and (s[1] == "1" or s[1] == "2" or s[1] == "3"):
        s = list(map(int,list(step)))
        if game_field[s[1]-1][s[0]-1] != "  ":
            return False
        return True
    else:
        return False

def write_step(step, turn):
    """запись хода на игровое поле"""
    s = list(map(int,list(step)))
    game_field[s[1]-1][s[0]-1] = " X" if turn % 2 == 1 else " O"

def next_turn(field, turn):
    """ход игрока"""
    while True:
        step = input(f"Ход {'1' if turn % 2 == 1 else '2'} игрока: ")
        if str.lower(step) == "concede":
            break
        if check_step(step):
            break
        else:
            print("ошибка ввода")
    if str.lower(step) == "concede":
        end_game((turn % 2) + 1)
        return True
    write_step(step, turn)
    draw_field(game_field)
    if turn == 9 and not check_winner(game_field):
        end_game(3)
        return True

def check_winner(field):
    """проверка, есть ли победитель"""
    for i in range(3):
        check = []
        for j in range(3):
            check.append(field[i][j])
        if check == [" X", " X", " X"] or check == [" O", " O", " O"]:
            return 1 if check[0] == " X" else 2
    check = []
    for j in range(3):
        check = []
        for i in range(3):
            check.append(game_field[i][j])
        if check == [" X", " X", " X"] or check == [" O", " O", " O"]:
            return 1 if check[0] == " X" else 2
    check = []
    for i in range(3):
        check.append(game_field[i][i])
    if check == [" X", " X", " X"] or check == [" O", " O", " O"]:
        return 1 if check[0] == " X" else 2
    check = []
    for i in range(3):
        check.append(game_field[i][2-i])
    if check == [" X", " X", " X"] or check == [" O", " O", " O"]:
        print("у нас есть победитель")
        return 1 if check[0] == " X" else 2

def start_game():
    """старт игры, обнуление игрового поля и счетчика ходов"""
    os.system('cls||clear')
    global game_field
    game_field = [["  ","  ","  "], ["  ","  ","  "], ["  ","  ","  "]]
    turn = 1
    draw_field(game_field)
    while not check_winner(game_field):
        if next_turn(game_field, turn):
            break
        turn += 1
    if check_winner(game_field):
        end_game(check_winner(game_field))

def end_game(winner):
    """конец игры и вывод победителя. предложение сыграть еще раз"""
    print("Игра окончена")
    if winner == 3:
        print("Ничья")
    else:
        print(f"Победил {winner} игрок")
    while True:
        end = input("Желаете сыграть еще раз? (Y/N): ")
        if str.lower(end) == "y":
            break
        elif str.lower(end) == "n":
            break
        else:
            print("Ошибка ввода")
    if str.lower(end) == "y":
        # os.system('cls||clear')
        start_game()

def help_page():
    print("""Координаты вводятся в виде двух цифр, первая указывает столбец, вторая - строку,
напимер 31:
  1 2 3
1     X
2
3
игрок может сдаться набрав concede, при этом победа будет засчитана другому игроку
нажмите Enter для возврата в меню""")
    input()
    start_menu()
start_menu()

