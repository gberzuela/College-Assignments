# othello_UI.py
# ICS 32 - Alex Thornton
# Gerald Berzuela - 27436118


import othello_gamelogic


def run_game() -> None:
    GameState = othello_gamelogic.Othello()

    while True:

        try:

            GameState.printScore(GameState._board)
            GameState.printBoard()
            GameState.printTurn()
            move, flipTiles = getMove(GameState, GameState._board)
            GameState.makeMove(move, flipTiles)
            
            boardCheck = GameState.checkBoard(GameState._board)
            
            if boardCheck is True: # If the opposite player can move, switch turns
                GameState.switchTurn()
            else:                  # Else, so not switch turns and continue forward
                continue

        except othello_gamelogic.GameOverError:
            return


def getMove(GameState: othello_gamelogic.Othello, board: [[int]]) -> None:
    '''
    Asks the user in a 'row column' format and splits it into a list
    Checks the input if they're valid rows/columns
    Checks the input if it's a valid move
    '''

    while True:
        
        try:
            move = input()

            GameState.checkInput(move.split())
            GameState.checkTile(move.split())
            flipTiles = GameState.isValidMove(GameState._turn, move.split())

            if len(flipTiles) != 0:
                print('VALID')
                return move.split(), flipTiles
            else:
                print('INVALID')
                continue

        except othello_gamelogic.InvalidRowColumn:
            print('INVALID')

        except othello_gamelogic.InvalidMoveError:
            print('INVALID')

        except ValueError:
            print('INVALID')

        except IndexError:
            print('INVALID')

        except TypeError:
            print('INVALID')
    
    
if __name__ == '__main__':
    print('FULL')
    run_game()
