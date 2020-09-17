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
    x = 0
    o = 0
    for char in cells:
        if char == 'X':
            x += 1
        if char == 'O':
            o += 1
    if x == o:
        return 'X'
    if x == o + 1:
        return 'O'

def board(cells):
    for i in range(9):
        if cells[i] == "_":
            cells[i] = " "
    print("---------")
    print("| {} {} {} |".format(*cells[0:4]))
    print("| {} {} {} |".format(*cells[3:6]))
    print("| {} {} {} |".format(*cells[6:9]))
    print("---------")

def states(cells):
    if ['O', 'O', 'O'] in [
                            cells[0:3], # horizontal
                            cells[3:6], 
                            cells[6:9], 
                            [cells[0], cells[3], cells[6]], # vertical
                            [cells[1], cells[4], cells[7]], 
                            [cells[2], cells[5], cells[8]],
                            [cells[0], cells[4], cells[8]], # diagonal
                            [cells[6], cells[4], cells[2]]
                          ]:
        return "O wins"
    elif ['X', 'X', 'X'] in [
                            cells[0:3], # horizontal
                            cells[3:6], 
                            cells[6:9], 
                            [cells[0], cells[3], cells[6]], # vertical
                            [cells[1], cells[4], cells[7]], 
                            [cells[2], cells[5], cells[8]], 
                            [cells[0], cells[4], cells[8]], # diagonal
                            [cells[6], cells[4], cells[2]]
                          ]:
        return "X wins"
        
    if not any([True for char in cells if char == " "]):
        return "Draw"
        
    else:
        return "Game not finished"


def main():
    print("Enter cells:")
    cells = list(input())
    board(cells)

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
                if cells[coords[coordinates_key]] != " ":
                    print("This cell is occupied! Choose another one!")
                else:
                    correct_input = True
            else:
                print("Coordinates should be from 1 to 3!")
                
    print(cells, coords[coordinates_key])
    cells[coords[coordinates_key]] = players_char(cells)
    board(cells)
    print(states(cells))

if __name__ == "__main__":
    main()