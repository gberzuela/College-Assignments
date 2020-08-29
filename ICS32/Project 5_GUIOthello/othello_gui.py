# othello_gui.py
# ICS 32 - Alex Thornton
# Gerald Berzuela - 27436118


import tkinter
import othello_options_board
import othello_gamelogic


DEFAULT_FONT = ('Helvetica', 12)


class OthelloGUI:
    def __init__(self):
        self._root_window = tkinter.Tk()
        self.game_start = False

        ''' Game edition frame '''
        ed_frame = tkinter.Frame(
            master = self._root_window, background = 'white', relief = tkinter.RIDGE, borderwidth = 4)

        ed_frame.grid(
            row = 0, column = 0, padx = 0, pady = 0,
            sticky = tkinter.W + tkinter.E)

        ''' Prompts frame '''
        self.prompts_frame = tkinter.Frame(
            master = self._root_window, background = 'white', relief = tkinter.RIDGE, borderwidth = 4)

        self.prompts_frame.grid(
            row = 1, column = 0, padx = 0, pady = 0,
            sticky = tkinter.W + tkinter.E)

        ''' Game frame '''
        canvas_frame = tkinter.Frame(
            master = self._root_window, background = 'blue')

        canvas_frame.grid(
            row = 2, column = 0, padx = 0, pady = 0,
            sticky = tkinter.N + tkinter.S + tkinter.W + tkinter.E)
        
        ''' Game canvas '''
        self._game_board_canvas = tkinter.Canvas(
            master = canvas_frame,
            width = 500, height = 500,
            background = 'green')

        self._game_board_canvas.grid(
            row = 0, column = 0, padx = 0, pady = 0,
            sticky = tkinter.N + tkinter.S + tkinter.W + tkinter.E)

        ''' Game edition label '''
        ed = tkinter.Label(
            master = ed_frame, background = 'white' ,
            text = 'FULL Version',
            font = DEFAULT_FONT)
        
        ed.grid(
            row = 0, column = 0,
            sticky = tkinter.E + tkinter.W)

        ''' Prompts label '''
        self.prompt = tkinter.Label(
            master = self.prompts_frame, background = 'white',
            text = 'Welcome to a game of Othello! Click anywhere in the green to begin.',
            font = DEFAULT_FONT)

        self.prompt.grid(
            row = 0, column = 0,
            sticky = tkinter.E + tkinter.W)

        ''' Any click on the initial canvas will open the options window '''
        self._game_board_canvas.bind('<Button-1>', self._on_options_clicked)

        ''' Redraws canvas on resize '''
        canvas_frame.bind('<Configure>', self._on_canvas_resized)
        
        self._root_window.rowconfigure(2, weight = 1)
        self._root_window.columnconfigure(0, weight = 1)

        canvas_frame.rowconfigure(0, weight = 1)
        canvas_frame.columnconfigure(0, weight = 1)

        ed_frame.rowconfigure(0, weight = 1)
        ed_frame.columnconfigure(0, weight = 1)

        self.prompts_frame.rowconfigure(0, weight = 1)
        self.prompts_frame.columnconfigure(0, weight = 1)


    def _on_options_clicked(self, event: tkinter.Event()) -> None:
        ''' Opens a new window that will return values for the gamestate '''
        options = othello_options_board.BoardOptions()
        options.show()

        self.GameState = othello_gamelogic.Othello()

        if options._ok_clicked:
            self.GameState._rows = options.get_row_number()
            self.GameState._columns = options.get_column_number()
            
            self.GameState._turn = options.get_first_player()
            ''' Defaults if nothing was selected '''
            if self.GameState._turn == 0:
                self.GameState._turn = 'B'
                
            self.GameState._winCon = options.get_win_con()
            ''' Defaults if nothing was selected '''
            if self.GameState._winCon == 0:
                self.GameState._winCon = '>'

            self.GameState.make_board(self.GameState._rows, self.GameState._columns)

            self.game_start = True

            self._draw_board()
            
            self._place_starting_pieces()


    def _draw_board(self) -> None:
        ''' Draws the grid '''
        self._game_board_canvas.delete(tkinter.ALL)

        width = self._game_board_canvas.winfo_width() / self.GameState._columns
        height = self._game_board_canvas.winfo_height() / self.GameState._rows

        for x in range(self.GameState._columns):
            for y in range(self.GameState._rows):
                x1 = x * width
                y1 = y * height
                x2 = x1 + width
                y2 = y1 + height
                self._game_board_canvas.create_rectangle(x1, y1, x2, y2)


    def _draw_pieces(self) -> None:
        ''' Searched through the game board to see if players have pieces and draws them '''
        width = self._game_board_canvas.winfo_width() / self.GameState._columns
        height = self._game_board_canvas.winfo_height() / self.GameState._rows

        for col in range(self.GameState._columns):
            counter = 0
            
            while counter < self.GameState._rows:

                x1 = col * width
                y1 = counter * height
                x2 = (col + 1) * width
                y2 = (counter + 1) * height
                
                if self.GameState._board[counter][col] == othello_gamelogic.BLACK:
                    self._game_board_canvas.create_oval(x1, y1, x2, y2, fill = 'black')
                elif self.GameState._board[counter][col] == othello_gamelogic.WHITE:
                    self._game_board_canvas.create_oval(x1, y1, x2, y2, fill = 'white')
                counter +=1  


    def _place_starting_pieces(self) -> None:
        ''' Binds the entire canvas to an event to place pieces for players '''
        self._game_board_canvas.bind('<Button-1>', self._starting_grid_click)
        self.prompt.configure(text = '')

        ''' Button to switch turns placing initial pieces '''
        self._initialize_game_button = tkinter.Button(
            master = self.prompts_frame, background = 'white', relief = tkinter.RIDGE,
            text = 'Player 1, place your pieces. Click here to switch turns.',
            font = DEFAULT_FONT, command = self._change_starting_piece_color)

        self._initialize_game_button.grid(
            row = 0 ,column = 0, padx = 0, pady = 0,
            sticky = tkinter.E + tkinter.W)


    def _change_starting_piece_color(self) -> None:
        ''' Button press for when players switch turns placing initial pieces '''
        self.GameState.switchTurn()
        self._initialize_game_button.configure(
            text = 'Player 2, place your pieces. Click here to start game.', command = self._start_game)


    def _starting_grid_click(self, event: tkinter.Event) -> None:
        ''' Gets where user clicked and changes the piece within the board '''
        width = self._game_board_canvas.winfo_width() / self.GameState._columns
        height = self._game_board_canvas.winfo_height() / self.GameState._rows

        grid_col = int(event.x / width)
        grid_row = int(event.y / height)
        
        if self.GameState._turn == othello_gamelogic.BLACK:
            self.GameState._board[grid_row][grid_col] = othello_gamelogic.BLACK
        elif self.GameState._turn == othello_gamelogic.WHITE:
            self.GameState._board[grid_row][grid_col] = othello_gamelogic.WHITE

        self._draw_pieces()


    def _on_grid_click(self, event: tkinter.Event) -> None:
        ''' Checks where the user clicked and determines if that is a valid move '''
        width = self._game_board_canvas.winfo_width() / self.GameState._columns
        height = self._game_board_canvas.winfo_height() / self.GameState._rows

        grid_col = int(event.x / width)
        grid_row = int(event.y / height)

        try:

            self.GameState.checkTile([grid_row, grid_col])
            self._check_move(grid_row, grid_col)
            self._check_winner()
            self._draw_board()
            self._draw_pieces()

        except othello_gamelogic.GameOverError:
            self._game_over_prompt()

        except othello_gamelogic.InvalidMoveError:
            self._error_prompt()


    def _check_move(self, grid_row: int, grid_col: int) -> None:
        ''' Goes checks the board in eight directions to create a list of flippable tiles '''
        flipTiles = self.GameState.isValidMove(self.GameState._turn, [grid_row, grid_col])
        if flipTiles == []:
            raise othello_gamelogic.InvalidMoveError()
        else:
            self.GameState.makeMove([grid_row, grid_col], flipTiles)
        

    def _check_winner(self) -> True:
        ''' Refer to othello_gamelogic on how checking for winner works '''
        try:
            
            boardCheck = self.GameState.checkBoard(self.GameState._board)
            if boardCheck is True:
                self.GameState.switchTurn()
                self._scoreboard_prompt()
                return True
            elif boardCheck is False:
                self._scoreboard_prompt()
                return False

        except othello_gamelogic.GameOverError:
            self._game_over_prompt()
                

    def _scoreboard_prompt(self) -> None:
        ''' Gets the score for each player and changes prompt according to whose turn it is '''
        blackScore, whiteScore = self.GameState.getScore(self.GameState._board)
        if self.GameState._turn is othello_gamelogic.BLACK:
            self.prompt.configure(text = f'Black: {blackScore}      TURN: Black      White: {whiteScore}')
        elif self.GameState._turn is othello_gamelogic.WHITE:
            self.prompt.configure(text = f'Black: {blackScore}      TURN: White      White: {whiteScore}')


    def _error_prompt(self) -> None:
        ''' Whenever there is an invalid move error, these prompts display '''
        if self.GameState._turn is othello_gamelogic.BLACK:
            self.prompt.configure(text = 'TURN: Black   INVALID MOVE')
        elif self.GameState._turn is othello_gamelogic.WHITE:
            self.prompt.configure(text = 'TURN: WHITE   INVALID MOVE')


    def _game_over_prompt(self) -> None:
        ''' When game is over, these prompts will be displayed '''
        blackScore, whiteScore = self.GameState.getScore(self.GameState._board)
        if self.GameState.winner is othello_gamelogic.BLACK:
            self.prompt.configure(text = f'Black: {blackScore}      WINNER: Black      White: {whiteScore}')
        elif self.GameState.winner is othello_gamelogic.WHITE:
            self.prompt.configure(text = f'Black: {blackScore}      WINNER: White      White: {whiteScore}')
        elif self.GameState.winner is othello_gamelogic.NONE:
            self.prompt.configure(text = f'Black: {blackScore}      WINNER: None      White: {whiteScore}')

        self._game_board_canvas.bind('<Button-1>', self._game_over_click)


    def _game_over_click(self, event: tkinter.Event) -> None:
        return


    def _start_game(self) -> None:
        ''' After player two places their pieces, the game switches turns again and proceeds '''
        self._check_winner()
        self.GameState.switchTurn()
        self._initialize_game_button.destroy()  # Gets rid of the button for the prompts
        self._scoreboard_prompt() 
        self._game_board_canvas.bind('<Button-1>', self._on_grid_click)

            
    def _on_canvas_resized(self, event: tkinter.Event) -> None:
        ''' Checks to see if game started, initializes game board then proceeds '''
        if not self.game_start:
            return
        self._draw_board()
        self._draw_pieces()
        

    def run(self):
        self._root_window.mainloop()

if __name__ == '__main__':
    game = OthelloGUI()
    game.run()
