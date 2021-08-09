# tic tac toe

board = [
    ["-", "-", "-"],
    ["-", "-", "-"],
    ["-", "-", "-"]
]

# print out the initial borad of the game
# ? all the variables can be put in print function
# ? what is the f"{}" about


def print_board(board):
    for row in board:
        for slot in row:
            print(f"{slot} ", end="")
        print()


user = True  # when true it refers to x, otherwise o
# print_board(board)


def quit(user_input):
    if user_input == "q":
        print("Thanks for playing")
        return True
    else:
        return False


def check_input(user_input):
    # check if its a number
    if not isnum(user_input):
        return False
    user_input = int(user_input)
    # check if its 1 - 9
    if not bounds(user_input):
        return False

    return True

# isnumeric() checks if a string is a number


def isnum(user_input):
    if not user_input.isnumeric():
        print("This is not a valid number")
        return False
    else:
        return True


def bounds(user_input):
    if user_input > 9 or user_input < 1:
        print("This numbe is out of bounds.")
        return False
    else:
        return True


def istaken(coords, board):
    row = coords[0]
    col = coords[1]
    if board[row][col] != "-":
        print("This position is already taken.")
        return True


def add_to_board(coords, board):
    row = coords[0]
    col = coords[1]
    board[row][col] = "x"


def coordinates(user_input):
    row = int(user_input / 3)
    col = user_input
    if col > 2:
        col = int(col % 3)
    return (row, col)


def current_user(user):
    if user:
        return "x"
    else:
        return "o"


while True:

    print_board(board)
    user_input = input(
        "Please enter a position 1 through 9 or enter \"q\" to quit")
    if quit(user_input):
        break
    if not check_input(user_input):
        print("Please try again.")
        continue
    user_input = int(user_input) - 1
    coords = coordinates(user_input)
    #board[0][0] = "x"
    if istaken(coords, board):
        print("Please try again.")
        continue
    add_to_board(coords, board)
    user = not user
