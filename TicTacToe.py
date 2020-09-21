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


def main():
    print("Enter cells:")
    cells = list(input())
    cells = [" " if cells[i] == "_" else cells[i] for i in range(9)]
    print_board(cells)

    correct_input = False
    
    while not correct_input:
        print("Enter the coordinates: ")
        coordinates = input().split(" ")
        print(coordinates)

        if len(coordinates) != 2:
            print("You should enter numbers!")
        elif len(coordinates[0]) != 1 or len(coordinates[1]) != 1:
            print("You should enter numbers!")
        else:
            if coordinates[0] and coordinates[1] in ['1', '2', '3']:
                coordinates_key = "({}, {})".format(*coordinates)
                print(cells[coords[coordinates_key]])
                if cells[coords[coordinates_key]] != " ":
                    print("This cell is occupied! Choose another one!")
                else:
                    correct_input = True
            else:
                print("Coordinates should be from 1 to 3!")
                
    cells[coords[coordinates_key]] = players_char(cells)
    print_board(cells)
    print(states(cells))

if __name__ == "__main__":
    main()