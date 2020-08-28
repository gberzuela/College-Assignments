import collections
import connectfour
import connectfour_mechanics


def connectfour_console_version() -> None:
    connectfour_mechanics.welcome_and_instructions()
    game_state = connectfour.new_game()
    connectfour_mechanics.print_game_state(game_state)
    
    while True:
        move_choice = connectfour_mechanics.pop_or_drop(game_state)
        column_number = connectfour_mechanics.get_column_number()
        
        if move_choice == 1:
            game_state = connectfour_mechanics.pop_choice(game_state, column_number)
        elif move_choice == 2:
            game_state = connectfour_mechanics.drop_choice(game_state, column_number)
            
        connectfour_mechanics.print_game_state(game_state)
        turn_result = connectfour.winner(game_state)
        
        if turn_result == 1:
            connectfour_mechanics.red_wins()
            break
        elif turn_result == 2:
            connectfour_mechanics.yellow_wins()
            break


if __name__ == '__main__':
    connectfour_console_version()
