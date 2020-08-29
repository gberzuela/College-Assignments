# othello_gamelogic.py
# ICS 31 - Alex Thornton
# Gerald Berzuela - 27436118


''' For turn/piece purposes '''
NONE = '.'
BLACK = 'B'
WHITE = 'W'


class InvalidRowColumn(Exception):
    ''' Raised when user inputs invalid row or column '''
    pass


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
        self._rows = self.rows()
        self._columns = self.columns()
        self._turn = self.getFirstTurn()
        self._winCon = self.getWinCondition()

        for rows in range(self._rows):
            row = input().split()
            self._board.append(row)

    
    def rows(self) -> int:
        ''' Gets user input for number of rows '''
        
        while True:
            
            try:
                rows = int(input())

                if rows % 2 != 0 or 16 < rows < 4:
                    print('INVALID')
                else:
                    return rows

            except ValueError:
                print('INVALID')


    def columns(self) -> int:
        ''' Gets user input for number of columns '''

        while True:
            
            try:
                columns = int(input())

                if columns % 2 != 0 or 16 < columns < 4:
                    print('INVALID')
                else:
                    return columns

            except ValueError:
                print('INVALID')


    def getWinCondition(self) -> str:
        ''' Gets a win condition < or > '''
    
        while True:
            winCondition = input()

            if winCondition != '>' and winCondition != '<':
                print('INVALID')
            else:
                return winCondition


    def printBoard(self) -> None:
        ''' Goes through each sublist printing each subsequent object '''
        
        for row in range(self._rows):
            for column in range(self._columns):
                if column + 1 != self._columns:
                    if self._board[row][column] is NONE:
                        print('. ', end = '')
                    elif self._board[row][column] is BLACK:
                        print('B ', end = '')
                    elif self._board[row][column] is WHITE:
                        print('W ', end = '')
                else:
                    if self._board[row][column] is NONE:
                        print('.', end = '')
                    elif self._board[row][column] is BLACK:
                        print('B', end = '')
                    elif self._board[row][column] is WHITE:
                        print('W', end = '')
                    
            print()

    ''' Test board '''

##    def makeBoard(self, rows: int, columns: int) -> [[int]]:
##        '''
##        Creates a two-dimensional list for printing purposes
##        Rows = number of sublists
##        Columns = number of objects in a sublist
##        '''
##        
##        board = []
##
##        for row in range(rows):
##            board.append([])
##            for column in range(columns):
##                board[row].append(0)
##
##        ''' Starting pieces for test purposes '''
##
##        board[int(rows / 2) - 1][int(columns / 2) - 1] = 1
##        board[int(rows / 2)][int(columns / 2)] = 1
##        board[int(rows / 2) - 1][int(columns / 2)] = 2
##        board[int(rows / 2)][int(columns / 2) - 1] = 2
##
##        return board


# Score
    def printScore(self, board: [[int]]) -> None:
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

        print(f'B: {scoreBlack}  W: {scoreWhite}')


# Turn
    def getFirstTurn(self) -> int:
        ''' Determines the first turn '''

        while True:
            
            try:
                firstTurn = str(input())

                if firstTurn != 'B' and firstTurn != 'W':
                    print('INVALID')
                elif firstTurn == 'B':
                    return BLACK
                elif firstTurn == 'W':
                    return WHITE
                
            except TypeError:
                print('INVALID')
                

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


    def printTurn(self) -> None:
        ''' Prints the current turn '''

        if self._turn is BLACK:
            print('TURN: B')
        elif self._turn is WHITE:
            print('TURN: W')


# Moves
    def checkInput(self, move: [str]) -> None:
        '''
        Takes list from splitting the user move input
        Checks each object if it is within the boards limits
        Catches errors and raises exceptions
        '''
                
        if self._rows < int(move[0]) or int(move[0]) < 0:
            raise InvalidRowColumn()
        elif self._columns < int(move[1]) or int(move[1]) < 0:
            raise InvalidRowColumn()


    def checkTile(self, move: [str]) -> None:
        ''' Checks to see if user input is a placed tile '''

        if self._board[int(move[0]) - 1][int(move[1]) - 1] is not NONE:
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

        rMove, cMove = int(move[0]) - 1, int(move[1]) - 1 # Starting point (row and column points)

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

##        print(flipTiles)

        return flipTiles


    def makeMove(self, move: [int], flipTiles: [[int]]) -> None:
        '''
        Places the players piece in first.
        Then goes through a list of valid pieces and places those
        '''
        
        self._board[int(move[0]) - 1][int(move[1]) - 1] = self._turn

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

        noneSpace = 0
        leftOver = []

        for i in range(len(board)):
            for j in range(len(board[i])):
                if board[i][j] == NONE:
                    noneSpace += 1
                    leftOver.append([int(i), int(j)])

        if noneSpace == 0:
            self.checkWinner(board)
            raise GameOverError()
        else:
            check1 = _op_player_moves(self, leftOver)
            check2 = _player_moves(self, leftOver)

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

        self.printScore(board) # Formatting purposes
        self.printBoard()
        
                    
        if self._winCon is '>':
            if scoreBlack > scoreWhite:
                print('WINNER: BLACK')
            elif scoreWhite > scoreBlack:
                print('WINNER: WHITE')
            else:
                print('WINNER: NONE')
        elif self._winCon is '<':
            if scoreBlack < scoreWhite:
                print('WINNER: BLACK')
            elif scoreWhite < scoreBlack:
                print('WINNER: WHITE')
            else:
                print('WINNER: NONE')
                
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
        a = GameState.isValidMove(GameState._turn, [piece[0] + 1, piece[1] + 1])
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
        a = GameState.isValidMove(GameState._turn, [piece[0] + 1, piece[1] + 1])
        if len(a) != 0:
            validPieces += 1
        
    if validPieces > 0:
        return True
    elif validPieces == 0:
        return False
