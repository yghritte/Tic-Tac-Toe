import random

coords = {'(1, 3)' : 0, 
          '(2, 3)' : 1, 
          '(3, 3)' : 2,
          '(1, 2)' : 3,
          '(2, 2)' : 4,
          '(3, 2)' : 5,
          '(1, 1)' : 6,
          '(2, 1)' : 7,
          '(3, 1)' : 8}    


def players_char(cells):
    x = cells.count('X')
    o = cells.count('O')
    if x == o:
        return 'X'
    if x == o + 1:
        return 'O'


def print_board(cells):
    print("---------")
    print("| {} {} {} |".format(*cells[0:4]))
    print("| {} {} {} |".format(*cells[3:6]))
    print("| {} {} {} |".format(*cells[6:9]))
    print("---------")


def states(cells):
    winning_positions = [cells[0:3], cells[3:6], cells[6:9],       # horizontal
                        cells[0:7:3], cells[1:8:3], cells[2:9:3],  # vertical
                        cells[0:9:4], cells[2:7:2]]                # diagonal

    if ['O', 'O', 'O'] in winning_positions:
        return "O wins"

    elif ['X', 'X', 'X'] in winning_positions:
        return "X wins"
        
    elif not any([True for char in cells if char == " "]):
        return "Draw"
        
    else:
        return "Game not finished"


def user_move(cells):
    correct_input = False
    while not correct_input:
        print("Enter the coordinates: ")
        coordinates = input().split(" ")

        if len(coordinates) != 2:
            print("You should enter numbers!")

        elif len(coordinates[0]) != 1 or len(coordinates[1]) != 1:
            print("You should enter numbers!")

        else:
            if coordinates[0] in ['1', '2', '3'] and coordinates[1] in ['1', '2', '3']:
                coordinates_key = "({}, {})".format(*coordinates)

                if cells[coords[coordinates_key]] != " ":
                    print("This cell is occupied! Choose another one!")

                else:
                    correct_input = True
                    cells[coords[coordinates_key]] = players_char(cells)
                    print_board(cells)
            else:
                print("Coordinates should be from 1 to 3!")


def AI_easy_move(cells):
    print('Making move level "easy"')
    allowed_pos = [i for i in range(9) if cells[i] == " "]
    random_point = random.choice(allowed_pos)
    cells[random_point] = players_char(cells)
    print_board(cells)


def AI_medium_move(cells):
    pass


def AI_hard_move(cells):
    pass


def start_game(player1, player2):
    cells = [" "] * 9
    print_board(cells)

    while states(cells) == "Game not finished":
        if player1 == 'user':
            user_move(cells)
        
        else:
            AI_easy_move(cells)

        # checking if the game is over
        if states(cells) != "Game not finished":
            break
        
        if player2 == 'user':
            user_move(cells)

        else:
            AI_easy_move(cells)

    print(states(cells))


def main():
    exit_ = False
    correct_menu = False

    while not correct_menu and exit_ is False:
        print("Input command:")
        menu = input().split(" ")
        
        if menu[0] == 'exit':
            exit_ = True

        elif len(menu) != 3 and menu != 'exit':
            print("Bad parameters!")

        else:
            if menu[0] == 'start' and menu[1] in ['user','easy'] and menu[2] in ['user','easy']:
                player1 = menu[1]
                player2 = menu[2]

                start_game(player1, player2)

            else:
                print("Bad parameters!")


if __name__ == "__main__":
    main()

