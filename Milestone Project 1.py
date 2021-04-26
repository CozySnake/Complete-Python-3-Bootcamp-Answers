def display_field(field):
    print(" - - - - - - - - -  ")
    print("|  "+field[7]+"  |  "+field[8]+"  |  "+field[9]+"  |")
    print(" - - - - - - - - -  ")
    print("|  "+field[4]+"  |  "+field[5]+"  |  "+field[6]+"  |")
    print(" - - - - - - - - -  ")
    print("|  "+field[1]+"  |  "+field[2]+"  |  "+field[3]+"  |")
    print(" - - - - - - - - -  ")


def make_a_move(count, fields):
    if count == 1:
        num = input("Player 1, Make your move: ")
    else:
        num = input("Player 2, Make your move: ")
    while not num.isdigit():
        num = input("Not a digit: ")
    while num in fields:
        num = input("This field is already taken! Choose another one: ")
    fields.append(num)
    return int(num)


def x_or_o():
    pl1 = input("Player 1, Choose X or O: ").upper()
    while pl1 not in ["X", "O"]:
        pl1 = input("Only X and O: ").upper()
    if pl1 == "X":
        pl2 = "O"
    else:
        pl2 = "X"
    print(f"Player 1 uses {pl1} and Player 2 uses {pl2}")
    return pl1, pl2


def paint(field, index, painter):
    field[index] = painter
    display_field(field)
    return field


def painter(count, players):
    if count == 1:
        painter = players[0]
    else:
        painter = players[1]
    return painter


def win_check(count, field, mypainter):
    if field[1] == field[2] == field[3] == mypainter or field[4] == field[5] == field[6] == mypainter or field[7] == field[8] == field[9] == mypainter or field[1] == field[4] == field[7] == mypainter or field[2] == field[5] == field[8] == mypainter or field[3] == field[6] == field[9] == mypainter or field[1] == field[5] == field[9] == mypainter or field[3] == field[5] == field[7] == mypainter:
        game_over = True
        print("Game over")
        if count == 1:
            print("Player 2 wins")
        else:
            print("Player 1 wins")
        return game_over


def no_space(fields):
    if len(fields) == 9:
        no_space = True
        print("Game over")
        print("You have no field to play")
    else:
        no_space = False
    return no_space


def again():
    question = input("Do you want to play again? (Y or N) ").upper()
    while question not in ["Y", "N"]:
        question = input("To continue please choose either Y or N: ").upper()
    if question == 'Y':
        field = [' ']*10
        fields = []
        check(field, fields)
        


field = [' ']*10
fields = []

def check(field, fields):
    win = False
    no_more_space = False
    count = 1
    display_field(field)
    players = x_or_o()
    while not win and not no_more_space:
        mydigit = make_a_move(count, fields)
        mypainter = painter(count, players)
        field = paint(field, mydigit, mypainter)
        count = count % 2 + 1
        win = win_check(count, field, mypainter)
        no_more_space = no_space(fields)
    again() 
    return field


field = check(field, fields)
