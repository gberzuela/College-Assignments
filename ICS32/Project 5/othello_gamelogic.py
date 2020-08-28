# othello_gamelogic.py
# ICS 31 - Alex Thornton
# Gerald Berzuela - 27436118


''' For turn/piece purposes '''
NONE = 0
BLACK = 1
WHITE = 2


class InvalidMoveError(Exception):
    ''' Raised when move is invalid '''
    pass


class GameOverError(Exception):
    ''' Raised when game is over '''
    pass


class Othello:
# Board
    def __init__(self):
        ''' Initializes the game board '''
        
        self._board = []
        self._rows = 0
        self._columns = 0
        self._turn = 0
        self._winCon = 0
        self.winner = 0

    def check_rows(rows: int) -> bool:
        ''' Checks the users row input '''
        try:

            rows = int(rows)
            if rows % 2 != 0 or 16 < rows < 4:
                return False
            else:
                return True

        except ValueError:
            return False

    def check_columns(columns: int) -> int:
        ''' Checks the users column input '''
        try:

            columns = int(columns)
            if columns % 2 != 0 or 16 < columns < 4:
                return False
            else:
                return True

        except ValueError:
            return False


    def make_board(self, rows: int, columns: int) -> None:
        ''' Creates game board '''
        for row in range(self._rows):
            self._board.append([])
            for col in range(self._columns):
                self._board[row].append(NONE)

# Score
    def getScore(self, board: [[int]]) -> int:
        '''
        Search through the 2D board list
        If a piece is a player piece, a corresponding counter will increase
        '''
        
        scoreBlack = 0
        scoreWhite = 0

        for row in range(len(board)):
            for column in range(len(board[row])):
                if board[row][column] is BLACK:
                    scoreBlack += 1
                elif board[row][column] is WHITE:
                    scoreWhite += 1

        return str(scoreBlack), str(scoreWhite)

# Turn               
    def switchTurn(self) -> None:
        ''' Changes whose turn it is '''

        if self._turn is BLACK:
            self._turn = WHITE
        elif self._turn is WHITE:
            self._turn = BLACK
            

    def getOpTurn(self) -> None:
        ''' Returns the opposite turn '''

        if self._turn is BLACK:
            return WHITE
        else:
            return BLACK
            
# Moves
    def checkTile(self, move: [int]) -> None:
        ''' Checks to see if user input is a placed tile '''

        if self._board[move[0]][move[1]] is not NONE:
            raise InvalidMoveError()


    def isValidMove(self, turn: int, move: [str]) -> [[int]]:
        '''
        From a specified position,
            checks the eight directions to see if anything can be flipped
            with private functions that append to a list
        Prints 'VALID' or 'INVALID' according to list size
        '''

        flipTiles = []

        rCounter = 1
        cCounter = 1

        rMove, cMove = move[0], move[1] # Starting point (row and column points)

        if turn is BLACK: # Assigning a 'tile' variable to opposite color
            tile = WHITE  # to find those pieces
        else:
            tile = BLACK

        # Diagonals 
        _check_down_right(self, tile, flipTiles, rCounter, cCounter, rMove, cMove)
        _check_up_right(self, tile, flipTiles, rCounter, cCounter, rMove, cMove)
        _check_up_left(self, tile, flipTiles, rCounter, cCounter, rMove, cMove)
        _check_down_left(self, tile, flipTiles, rCounter, cCounter, rMove, cMove)
        # Cross
        _check_right(self, tile, flipTiles, rCounter, cCounter, rMove, cMove)
        _check_left(self, tile, flipTiles, rCounter, cCounter, rMove, cMove)
        _check_down(self, tile, flipTiles, rCounter, cCounter, rMove, cMove)
        _check_up(self, tile, flipTiles, rCounter, cCounter, rMove, cMove)

        return flipTiles


    def makeMove(self, move: [int], flipTiles: [[int]]) -> None:
        '''
        Places the players piece in first.
        Then goes through a list of valid pieces and places those
        '''
        
        self._board[move[0]][move[1]] = self._turn

        for i in range(len(flipTiles)):
            for j in range(len(flipTiles[i])):
                self._board[flipTiles[i][j][0]][flipTiles[i][j][1]] = self._turn
                
        
# Looking for winner
    def checkBoard(self, board: [[int]]) -> None:
        '''
        Checks if the board has any empty spaces left
            appens those coordinates to a list
        If there are, checks to see if they are valid for the next player
        If not, checks for the winner
        '''

        leftOver = []

        for i in range(len(board)):
            for j in range(len(board[i])):
                if board[i][j] == NONE:
                    leftOver.append([int(i), int(j)])

        print(leftOver)

        if len(leftOver) == 0:
            self.checkWinner(board)
            raise GameOverError()
        else:
            check1 = _op_player_moves(self, leftOver)
            check2 = _player_moves(self, leftOver)

            print(check1, check2)

            if check1 is True: # Opposite player can make a move
                return True
            elif check1 is False and check2 is True: # Opposite player can't make a move
                return False
            elif check1 is False and check2 is False:
                self.checkWinner(board)
                raise GameOverError()
            

    def checkWinner(self, board: [[int]]) -> None:
        ''' Counts each players piece and prints the winner '''

        scoreBlack = 0
        scoreWhite = 0

        for row in range(len(board)):
            for column in range(len(board[row])):
                if board[row][column] is BLACK:
                    scoreBlack += 1
                elif board[row][column] is WHITE:
                    scoreWhite += 1        
                    
        if self._winCon is 1:
            if scoreBlack > scoreWhite:
                self.winner = 1
            elif scoreWhite > scoreBlack:
                self.winner = 2
            else:
                self.winner = 0
        elif self._winCon is 2:
            if scoreBlack < scoreWhite:
                self.winner = 1
            elif scoreWhite < scoreBlack:
                self.winner = 2
            else:
                self.winner = 0
                
# Helper functions
def _check_down_right(GameState: Othello, tile: int, flipTiles: [], rCounter: int, cCounter: int, rMove: int, cMove: int) -> None:
    ''' Searches pieces down and right '''
    '''
    Following 8 functions are the same
    Checks the tile in the given direction (stated in the previous comment)
        if it is the opposite player's then appends coordinate to a list
    If the check runs across a tile of the current player's while the list
        containing coordinates to the opposite player's piece is not empty
        appends the current player's tile and ends the loop
    '''

    opPiece = [] # List of opposite pieces

    while rCounter <= GameState._rows - 1 and cCounter <= GameState._columns - 1:
        try:

            if rMove + rCounter < 0 or cMove + cCounter < 0: # Checks for edge of board
                return 
            elif tile == GameState._board[rMove + rCounter][cMove + cCounter]: 
                opPiece.append([rMove + rCounter, cMove + cCounter])
                rCounter += 1
                cCounter += 1
            elif len(opPiece) != 0 and GameState._board[rMove + rCounter][cMove + cCounter] == GameState._turn:
                opPiece.append([rMove + rCounter, cMove + cCounter])
                flipTiles.append(opPiece)
##                    print('down right')
                return 
            else:      # opPiece contains coordinates, but aren't flippable
                return # because the last piece isn't the current player's

        except IndexError: 
            return 


def _check_up_right(GameState: Othello, tile: int, flipTiles: [], rCounter: int, cCounter: int, rMove: int, cMove: int) -> None:
    ''' Searches pieces up and right '''

    opPiece = []

    while rCounter <= GameState._rows - 1 and cCounter <= GameState._columns - 1:
        
        try:

            if rMove - rCounter < 0 or cMove + cCounter < 0:
                return 
            elif tile == GameState._board[rMove - rCounter][cMove + cCounter]: 
                opPiece.append([rMove - rCounter,cMove + cCounter])
                rCounter += 1
                cCounter += 1
            elif len(opPiece) != 0 and GameState._board[rMove - rCounter][cMove + cCounter] == GameState._turn:
                opPiece.append([rMove - rCounter, cMove + cCounter])
                flipTiles.append(opPiece)
##                    print('up right')
                return 
            else:
                return 

        except IndexError:
            return 


def _check_up_left(GameState: Othello, tile: int, flipTiles: [], rCounter: int, cCounter: int, rMove: int, cMove: int) -> None:
    ''' Searches pieces up and left '''

    opPiece = []

    while rCounter <= GameState._rows - 1 and cCounter <= GameState._columns - 1:

        try:

            if rMove - rCounter < 0 or cMove - cCounter < 0:
                return 
            elif tile == GameState._board[rMove - rCounter][cMove - cCounter]:
                opPiece.append([rMove - rCounter, cMove - cCounter])
                rCounter += 1
                cCounter += 1
            elif len(opPiece) != 0 and GameState._board[rMove - rCounter][cMove - cCounter] == GameState._turn:
                opPiece.append([rMove - rCounter, cMove - cCounter])
                flipTiles.append(opPiece)
##                    print('up left')
                return 
            else:
                return 

        except IndexError:
            return 


def _check_down_left(GameState: Othello, tile: int, flipTiles: [], rCounter: int, cCounter: int, rMove: int, cMove: int) -> None:
    ''' Searches down and left '''

    opPiece = []

    while rCounter <= GameState._rows - 1 and cCounter <= GameState._columns - 1:

        try:
            
            if rMove + rCounter < 0 or cMove - cCounter < 0:
                return 
            elif tile == GameState._board[rMove + rCounter][cMove - cCounter]:
                opPiece.append([rMove + rCounter, cMove - cCounter])
                rCounter += 1
                cCounter += 1
            elif len(opPiece) != 0 and GameState._board[rMove + rCounter][cMove - cCounter] == GameState._turn:
                opPiece.append([rMove + rCounter, cMove - cCounter])
                flipTiles.append(opPiece)
##                    print('down left')
                return 
            else:
                return 

        except IndexError:
            return 
                

def _check_right(GameState: Othello, tile: int, flipTiles: [], rCounter: int, cCounter: int, rMove: int, cMove: int) -> None:
    ''' Searches right '''

    opPiece = []

    while rCounter <= GameState._rows - 1 and cCounter <= GameState._columns - 1:
        try:

            if rMove < 0 or cMove + cCounter < 0:
                return 
            elif tile == GameState._board[rMove][cMove + cCounter]: # Right
                opPiece.append([rMove, cMove + cCounter])
                rCounter += 1
                cCounter += 1
            elif len(opPiece) != 0 and GameState._board[rMove][cMove + cCounter] == GameState._turn:
                opPiece.append([rMove, cMove + cCounter])
                flipTiles.append(opPiece)
##                    print('right')
                return 
            else:
                return 

        except IndexError:
            return 


def _check_left(GameState: Othello, tile: int, flipTiles: [], rCounter: int, cCounter: int, rMove: int, cMove: int) -> None:
    ''' Searches left '''

    opPiece = []
    
    while rCounter <= GameState._rows - 1 and cCounter <= GameState._columns - 1:
        
        try:

            if rMove < 0 or cMove - cCounter < 0:
                return 
            elif tile == GameState._board[rMove][cMove - cCounter]: # Left
                opPiece.append([rMove, cMove - cCounter])
                rCounter += 1
                cCounter += 1
            elif len(opPiece) != 0 and GameState._board[rMove][cMove - cCounter] == GameState._turn:
                opPiece.append([rMove, cMove - cCounter])
                flipTiles.append(opPiece)
##                    print('left')
                return 
            else:
                return 

        except IndexError:
            return 


def _check_down(GameState: Othello, tile: int, flipTiles: [], rCounter: int, cCounter: int, rMove: int, cMove: int) -> None:
    ''' Searches down '''

    opPiece = []
    
    while rCounter <= GameState._rows - 1 and cCounter <= GameState._columns - 1:
        
        try:

            if rMove + rCounter < 0 or cMove < 0:
                return 
            elif tile == GameState._board[rMove + rCounter][cMove]: # Down
                opPiece.append([rMove + rCounter, cMove])
                rCounter += 1
                cCounter += 1
            elif len(opPiece) != 0 and GameState._board[rMove + rCounter][cMove] == GameState._turn:
                opPiece.append([rMove + rCounter, cMove])
                flipTiles.append(opPiece)
##                    print('down')
                return 
            else:
                return 

        except IndexError:
            return 


def _check_up(GameState: Othello, tile: int, flipTiles: [], rCounter: int, cCounter: int, rMove: int, cMove: int) -> None:
    ''' Searches up '''

    opPiece = []
    
    while rCounter <= GameState._rows - 1 and cCounter <= GameState._columns - 1:
        
        try:

            if rMove - rCounter < 0 or cMove < 0:
                return
            elif tile == GameState._board[rMove - rCounter][cMove]: # Up
                opPiece.append([rMove - rCounter, cMove])
                rCounter += 1
                cCounter += 1
            elif len(opPiece) != 0 and GameState._board[rMove - rCounter][cMove] == GameState._turn:
                opPiece.append([rMove - rCounter, cMove])
                flipTiles.append(opPiece)
##                    print('up')
                return
            else:
                return


        except IndexError:
            return
        

def _op_player_moves(GameState: Othello, leftOver: [[int]]) -> bool:
    ''' Checks valid moves for the opposite player '''

    GameState.switchTurn() # Switch the turn to check for valid moves for the opposite player
    validPieces = 0

    for piece in leftOver:
        a = GameState.isValidMove(GameState._turn, [piece[0], piece[1]])
        if len(a) != 0:
            validPieces += 1
        
    if validPieces > 0:
        GameState.switchTurn() 
        return True
    elif validPieces == 0:
        GameState.switchTurn()
        return False


def _player_moves(GameState: Othello, leftOver: [[int]]) -> bool:
    ''' Checks valid moves for current player '''

    validPieces = 0

    for piece in leftOver:
        a = GameState.isValidMove(GameState._turn, [piece[0], piece[1]])
        if len(a) != 0:
            validPieces += 1
        
    if validPieces > 0:
        return True
    elif validPieces == 0:
        return False
