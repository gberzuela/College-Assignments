import collections
import connectfour


def welcome_and_instructions() -> None:
    print('Welcome to a game of Connect Four.\n')
    print('The rules are simple:')
    print('The first player to place four pieces in a row')
    print('(horizontally, vertically, or diagonally) wins.\n')
    print('You will be given the option to either pop one of your own')
    print('pieces from the bottom of the desired column or')
    print('drop a piece into a desired column.\n')
    print("Let's get started\n")


def print_game_state(game_state: connectfour.GameState) -> None:
    for num in range(1, 8):
        print(num, '  ', end = '')
    print() 

    for i in range(connectfour.BOARD_ROWS):
        counter = 0
        while counter < connectfour.BOARD_COLUMNS:
            if game_state.board[counter][i] == 0:
                print('.   ', end = '')
            elif game_state.board[counter][i] == connectfour.RED:
                print('R   ', end = '')
            elif game_state.board[counter][i] == connectfour.YELLOW:
                print('Y   ', end = '')
            counter += 1
        print()
            
    print()


def pop_or_drop(game_state: connectfour.GameState) -> int:
    while True:
        try:
            pop_or_drop = int(input(f'Player {get_player_turn(game_state)} Would you like to Pop(1) or Drop(2)? '))
            if pop_or_drop < 1 or pop_or_drop > 2:
                print('Invalid option.')
            else:
                return pop_or_drop
        except ValueError:
            print('Invalid option.\n')


def pop_choice(game_state: connectfour.GameState, column_number: int) -> connectfour.GameState:
    try:
        game_state = connectfour.pop(game_state, column_number)
    except connectfour.InvalidMoveError:
        print('Invalid move.\n')
    return game_state


def drop_choice(game_state: connectfour.GameState, column_number: int) -> connectfour.GameState:
    try:
        game_state = connectfour.drop(game_state, column_number)
    except connectfour.InvalidMoveError:
        print('Invalid move.\n')
    return game_state


def get_player_turn(game_state: connectfour.GameState) -> str:
    if game_state.turn == 1:
        return "RED"
    else:
        return "YELLOW"


def get_column_number() -> int:
    while True:
        try:
            column_number = int(input('Please select a column number: '))
            if column_number < 1 or column_number > 7:
                print('Invalid input.')
            else:
                print()
                return column_number - 1
        except ValueError:
            print('Invalid input.\n')


def red_wins() -> None:
    print('RED is the winner!\nThank you for playing!\nGood Bye!')


def yellow_wins() -> None:
    print('Yellow is the winner!\nThank you for playing!\nGood Bye!')

