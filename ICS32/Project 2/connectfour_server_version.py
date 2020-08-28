# Not complete. Could not figure out how to get all the data from socket.

import collections
import connectfour
import connectfour_mechanics
import connectfour_console
import connectfour_server_mechanics


class NotValidServerError(Exception):
    pass


def connectfour_server_version() -> None:
    #Initializes game. Also checks server response to see if receiving message is as expected
    try:
        game_state, connection = start_game()
    except NotValidServerError:
        return
    
    while True:
        #Player move
        move_choice = connectfour_mechanics.pop_or_drop(game_state)
        column_number = connectfour_mechanics.get_column_number()
        
        if move_choice == 1:
            game_state = connectfour_mechanics.pop_choice(game_state, column_number)
            connectfour_server_mechanics.send_user_message(connection, f'POP {column_number + 1}')
        elif move_choice == 2:
            game_state = connectfour_mechanics.drop_choice(game_state, column_number)
            connectfour_server_mechanics.send_user_message(connection, f'DROP {column_number + 1}')
            
        #Print current GameState and checks if user won
        connectfour_mechanics.print_game_state(game_state)
        check = check_for_winner(connection, game_state)
        if check is True:
            return
        
        #Server move
        AI_move = receive_message(connection)

        if 'OKAY' in AI_move or 'READY' in AI_move:
            AI_move.append(receive_message(connection))

            if 'DROP' in AI_move[1][0] or 'POP' in AI_move[1][0].split():
                AI_move.append(receive_message(connection))
                    
                print(f'AI Turn:\nMove: {AI_move[1][0].split()[0]}\nColumn: {AI_move[1][0].split()[1]}\n')

                if AI_move[1][0].split()[0] == 'DROP':
                    game_state = connectfour.drop(game_state, int(AI_move[1][0].split()[1]) - 1)
                elif AI_move[1][0].split()[0] == 'POP':
                    game_state = connectfour.pop(game_state, int(AI_move[1][0].split()[1]) - 1)
            
                #Print current GameState and checks is server won
                connectfour_mechanics.print_game_state(game_state)
                check = check_for_winner(connection, game_state)
                if check is True:
                    return

        elif 'INVALID' in AI_move:
            continue


def start_game() -> (connectfour.GameState, connectfour_server_mechanics.ConnectFourSocket):
    connectfour_server_mechanics.game_introduction() #Initial prompt and instructions
    game_state = connectfour.new_game() #Initializes new_game
    connection = connect_to_server() #Gets connection to user provided host and port
    send_username(connection) #Asks for username and checks servers response
    send_AI_game(connection) 
    connectfour_mechanics.print_game_state(game_state) 
    return game_state, connection


def connect_to_server() -> connectfour_server_mechanics.ConnectFourSocket:
    connection = connectfour_server_mechanics.connecting_interface()
    
    return connection


def send_username(connection: connectfour_server_mechanics.ConnectFourSocket) -> bool:
    message = 'I32CFSP_HELLO '
    username = input('Please enter a username: ')
    connectfour_server_mechanics.send_user_message(connection, message + username)
    server_message = receive_message(connection)
    print_server_message(server_message)
    if server_message != ['WELCOME' + ' ' + username]:
        print('Huh. It looks like you did not provide a valid Connect Four Server.\nProgram will end now. Goodbye!')
        connectfour_server_mechanics.close_connection(connection)
        raise NotValidServerError


def send_AI_game(connection: connectfour_server_mechanics.ConnectFourSocket) -> bool:
    connectfour_server_mechanics.send_user_message(connection, 'AI_GAME')
    message = receive_message(connection)
    print_server_message(message)
    print()  


def receive_message(connection: connectfour_server_mechanics.ConnectFourSocket) -> [str] or bool:
    server_message = []
    server_response = connectfour_server_mechanics.read_message(connection)
    server_message.append(server_response)

    return server_message


def print_server_message(message: [str]) -> None:
    for i in range(len(message)):
        print(message[i])
        
    print()


def check_for_winner(connection: connectfour_server_mechanics.ConnectFourSocket, game_state: connectfour.GameState) -> bool:
    turn_result = connectfour.winner(game_state)
    if turn_result == 1:
        connectfour_mechanics.red_wins()
        connectfour_server_mechanics.close_connection(connection)
        return True
    elif turn_result == 2:
        connectfour_mechanics.yellow_wins()
        connectfour_server_mechanics.close_connection(connection)
        return True
    else:
        return False

    
if __name__ == '__main__':
    connectfour_server_version()
