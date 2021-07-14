import random

def display_board(ttt_list):
    print(" ____ "*3)
    print(f"| {ttt_list[0]}  |"+f"| {ttt_list[1]}  |"+f"| {ttt_list[2]}  |")
    print(" ____ "*3)
    print(f"| {ttt_list[3]}  |"+f"| {ttt_list[4]}  |"+f"| {ttt_list[5]}  |")
    print(" ____ "*3)
    print(f"| {ttt_list[6]}  |"+f"| {ttt_list[7]}  |"+f"| {ttt_list[8]}  |")
    print(" ____ "*3)
def game_intro():
    print("Hello there!! welcome to Tic Tac Toe board game!!!")
    print("First, please take a careful observation to the game board, the number keys present their corresponding location on the board. ")
    display_board(default_list)
    print("when a number key is pressed, an X or O will be placed on its allocated position")
    start_signal = 'wrong'
    while start_signal !='yes':
        start_signal = input("Now, enter yes when you are ready to start the game: ")

def players():
    name1=input("please enter first person's name here: ")
    name2 = input("Please enter second person's name here: ")
    print(f"Nice! Now {name1} and {name2}, let's roll a dice to decide who goes first.")
    roll1 = 'wrong'
    while roll1 != 'roll':
        roll1 = input(f"{name1}, enter roll to roll the dice: ")
        if roll1 == 'roll':
            dice1 = random.randint(1,6)
            print(dice1)
    roll2 ='wrong'
    while roll2 !='roll':
        roll2 = input(f"{name2}, enter roll to roll the dice: ")
        if roll2 =='roll':
            dice2 = random.randint(1,6)
            print(dice2)
            while dice2 == dice1:
                print("Tie... dice automatically rerolled again]")
                dice2 = random.randint(1,6)
                print(dice2)
    if dice1>dice2:
        player1 = name1
        player2 = name2
        role1 = 'wrong'
        while (role1 != 'X') and (role1 !='O'):
            role1 = input(f'{player1}, you go first and choose your role as "X" or "O". Enter the corresponding letter key: ')
            if role1 == 'X':
                role2 = 'O'
                print(f'{player1} your role is now "{role1}". And unfortunately "{player2}" your role is "{role2}" because your have no choice left')
            elif role1 == 'O':
                role2 ='X'
                print(f'{player1} your role is now "{role1}". And unfortunately "{player2}" your role is "{role2}" because your have no choice left')
    elif dice2>dice1:
        player1 = name2
        player2 = name1
        role2 = 'wrong'
        while (role2 != 'X') and (role2 != 'O'):
            role2 = input(f'{player1}, you go first and choose your role as "X" or "O". Enter the corresponding letter key: ')
            if role2 == 'X':
                role1 = 'O'
                print(f'{player1} your role is now "{role2}". And unfortunately {player2} your role is "{role1}" because your have no choice left')
            elif role2 == 'O':
                role1 = 'X'
                print(f'{player1} your role is now "{role2}". And unfortunately {player2} your role is "{role1}" because your have no choice left')
    return player1, player2, role1, role2

def position_change(player,role):
    entered_key = 'wrong'
    while entered_key not in [1,2,3,4,5,6,7,8,9]:
        entered_key = int(input(f'{player}, please take your step now by entering the number key: '))
        while entered_key in decision_local:
            entered_key = int(input("Position is already taken. Try again: "))
        decision_local.append(entered_key)


    starting_list[entered_key-1] = role
    return starting_list

def game_check(list):
    if (list[0]==list[1] == list[2] != ' ') or (list[3] == list[4] == list[5] != ' ') or (list[6] ==list[7] ==list[8] != ' '):
        return True
    elif (list[0] == list[3] ==list[6] !=' ') or (list[1] == list[4]==list[7] != ' ') or (list[2]== list[5]== list[8]!= ' '):
        return True
    elif (list[0] == list[4] == list[8] !=' ') or (list[2] == list[4]==list[6] !=' '):
        return True
    else:
        return False
def game_on():
    choice = 'wrong'
    while choice not in ['Y', 'N']:
        choice = input("Enter Y to continue or N to end the game: ")
        if choice not in ['Y','N']:
            print("Sorry, I don't understand")
        elif choice == 'Y':
            return True
        elif choice == 'N':
            return False

def clear():
    print("\n"*100)

default_list = ["1","2","3","4","5","6","7","8","9"]
starting_list = [' ',' ',' ',' ',' ',' ',' ',' ',' ']
reset_list = [' ',' ',' ',' ',' ',' ',' ',' ',' ']
game_intro()
game_on1 = True
decision_local = [0]
reset_location = [0]
while game_on1:
    game_check1 = False
    game_check2 = False
    result = players()
    player1= result[0]
    player2= result[1]
    role1= result[2]
    role2 = result[3]
    for i in range(1,101):
        if game_check1 == True:
            print(f"{player1} won the game!")
            break
        elif game_check2 == True:
            print(f"{player2} won the game!")
            break
        elif len(decision_local) == 10:
            print("Game is tied!")
            break
        elif i%2 != 0:
            new_list = position_change(player1, role1)
            game_check1 = game_check(new_list)
            display_board(new_list)
        elif i%2 ==0:
            new_list = position_change(player2,role2)
            game_check2 = game_check(new_list)
            display_board(new_list)
    starting_list = reset_list
    decision_local = reset_location
    game_on1 = game_on()
    if game_on1 == True:
        clear()