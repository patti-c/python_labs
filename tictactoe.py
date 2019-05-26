def greet_user():
    print("Welcome to Tic Tac Toe")
    print("")

def create_state():
    return {
        "board": create_board(),
        "victory": False,
        "whose_turn": "O"
    }

def create_board():
    return [
        ["_", "_", "_"],
        ["_", "_", "_"],
        [" ", " ", " "]
    ]

def print_board(board=[]):
    for row in board:
        print_row(row)
    print("")

def print_row(row=[]):
    print("\t", end="")
    for (index, square) in enumerate(row):
        print_square(index, square)
    print("")

def print_square(index, square=''):
    if(index != 2):
        print(square, end="|")
    else: print(square, end="")

def is_empty(square):
    if(square == ' ' or square == "_"):
        return True

def run_game(state={}):
    board, victory, whose_turn = state.values()
    while victory != True:
        print_board(board)
        map = moves_mapped_to_board(board)
        print(f"Current Player's Turn: {whose_turn}\n")
        user_input = prompt_move(whose_turn, map)
        board = update_board(whose_turn, user_input, board)
        victory = check_for_victory(board)
        if(victory == True): break
        whose_turn = toggle_turn(whose_turn)
    print_board(board)
    print(f"Congratulations! The winner was {whose_turn}")
    pass

def prompt_move(whose_turn, map):

    user_input = input("Enter a number from 0 to 8 to select a square: ")
    if validate_move(map, user_input):
        return user_input
    else:
        return prompt_move(whose_turn, map)

def validate_move(map, user_input):
    valid_moves = ("0", "1", "2", "3", "4", "5", "6", "7", "8")
    if user_input in valid_moves and square_is_not_taken(map, user_input):
        return user_input
    else:
        print("That is not a valid move.")
        return False

def square_is_not_taken(map, user_input):
    if is_empty(map[user_input]):
        return True
    else:
        return False

def moves_mapped_to_board(board):
    return {
        "0": board[0][0],
        "1": board[0][1],
        "2": board[0][2],
        "3": board[1][0],
        "4": board[1][1],
        "5": board[1][2],
        "6": board[2][0],
        "7": board[2][1],
        "8": board[2][2]
    }

def update_board(whose_turn, user_input, board):
    switcher = {
        "0": lambda: update_square(board, 0, 0, whose_turn),
        "1": lambda: update_square(board, 0, 1, whose_turn),
        "2": lambda: update_square(board, 0, 2, whose_turn),
        "3": lambda: update_square(board, 1, 0, whose_turn),
        "4": lambda: update_square(board, 1, 1, whose_turn),
        "5": lambda: update_square(board, 1, 2, whose_turn),
        "6": lambda: update_square(board, 2, 0, whose_turn),
        "7": lambda: update_square(board, 2, 1, whose_turn),
        "8": lambda: update_square(board, 2, 2, whose_turn)
    }
    switcher[user_input]()
    return board

def update_square(board, x, y, value):
    board[x][y] = value

def check_for_victory(board):
    if(check_rows(board)): return True
    if(check_columns(board)): return True
    if(check_diagonals(board)): return True

def check_rows(board):
    return check_groups(board)

def check_columns(board):
    columns = [
        (board[0][0], board[1][0], board[2][0]),
        (board[0][1], board[1][1], board[2][1]),
        (board[0][2], board[1][2], board[2][2])
    ]
    return check_groups(columns)

def check_diagonals(board):
    diagonals = [
        (board[0][0], board[1][1], board[2][2]),
        (board[2][0], board[1][1], board[0][2])
    ]
    return check_groups(diagonals)

def check_groups(groups):
    for group in groups:
        if check_group(group):
            return True
            break

def check_group(group):
    if(group.count("O") == 3 or group.count("X") == 3): return True

def toggle_turn(whose_turn):
    switch = {
        "X" : "O",
        "O" : "X"
    }
    return switch[whose_turn]

def start_game():
    greet_user()
    state = create_state()
    run_game(state)

start_game()
