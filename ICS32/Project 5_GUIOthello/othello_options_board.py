# options_board.py
# ICS 32 - Alex Thornton
# Gerald Berzuela- 27436118


import tkinter
import othello_gamelogic


DEFAULT_FONT = ('Helvetica', 10)


class BoardOptions:
    def __init__(self):
        ''' Creating options window '''
        self._options_window = tkinter.Toplevel()

        self.options_label = tkinter.Label(
            master = self._options_window,
            text = 'Please enter game options.',
            font = DEFAULT_FONT)

        self.options_label.grid(
            row = 0, column = 0, columnspan = 2, padx = 10, pady =10,
            sticky = tkinter.N + tkinter.S + tkinter.E + tkinter.W)

        ''' Row input '''
        row_number_label = tkinter.Label(
            master = self._options_window,
            text = 'Row Number:',
            font = DEFAULT_FONT)

        row_number_label.grid(
            row = 1, column = 0, padx = 10, pady = 0,
            sticky = tkinter.W)

        self.row_number_entry = tkinter.Entry(
            master = self._options_window, width = 10, font = DEFAULT_FONT)

        self.row_number_entry.grid(
            row = 1, column = 1, padx = 10, pady = 1,
            sticky = tkinter.W  + tkinter.E)
        
        ''' Column input '''
        column_number_label = tkinter.Label(
            master = self._options_window,
            text = 'Column Number:',
            font = DEFAULT_FONT)

        column_number_label.grid(
            row = 2, column = 0, padx = 10, pady = 0,
            sticky = tkinter.W)

        self.column_number_entry = tkinter.Entry(
            master = self._options_window, width = 10, font = DEFAULT_FONT)

        self.column_number_entry.grid(
            row = 2, column = 1, padx = 10, pady = 1,
            sticky = tkinter.W  + tkinter.E)
        
        ''' First player radiobutton '''
        first_player_label = tkinter.Label(
            master = self._options_window,
            text = 'First Player:',
            font = DEFAULT_FONT)

        first_player_label.grid(
            row = 3, column = 0, padx = 10, pady = 0,
            sticky = tkinter.W)

        self.first_player = tkinter.IntVar()

        b_entry = tkinter.Radiobutton(
            master = self._options_window,
            text = 'Black', font = DEFAULT_FONT,
            variable = self.first_player,
            value = 1)

        b_entry.grid(
            row = 4, column = 0, padx = 10, pady = 0,
            sticky = tkinter.W)

        w_entry = tkinter.Radiobutton(
            master = self._options_window,
            text = 'White', font = DEFAULT_FONT,
            variable = self.first_player,
            value = 2)

        w_entry.grid(
            row = 5, column = 0, padx = 10, pady = 0,
            sticky = tkinter.W)

        ''' Win condition radiobutton '''
        win_con_label = tkinter.Label(
            master = self._options_window,
            text = 'Win Condition:',
            font = DEFAULT_FONT)

        win_con_label.grid(
            row = 3, column = 1, padx = 10, pady = 0,
            sticky = tkinter.W)

        self.win_con = tkinter.IntVar()

        less_than_entry = tkinter.Radiobutton(
            master = self._options_window,
            text = '>', font = DEFAULT_FONT,
            variable = self.win_con,
            value = 1)

        less_than_entry.grid(
            row = 4, column = 1, padx = 10, pady = 0,
            sticky = tkinter.W)

        greater_than_entry = tkinter.Radiobutton(
            master = self._options_window,
            text = '<', font = DEFAULT_FONT,
            variable = self.win_con,
            value = 2)

        greater_than_entry.grid(
            row = 5, column = 1, padx = 10, pady = 0,
            sticky = tkinter.W)
            
            
        ''' Ok and cancel buttons '''
        button_frame = tkinter.Frame(
            master = self._options_window)

        button_frame.grid(
            row = 6, column = 0, columnspan = 2, padx = 10, pady = 0,
            sticky = tkinter.E + tkinter.S)

        ok_button = tkinter.Button(
            master = button_frame, text = 'Ok', font = DEFAULT_FONT,
            command = self._on_ok_clicked)

        ok_button.grid(
            row = 0, column = 0, padx = 10, pady = 5,
            sticky = tkinter.E + tkinter.S)

        cancel_button = tkinter.Button(
            master = button_frame, text= 'Cancel', font = DEFAULT_FONT,
            command = self._on_cancel_clicked)

        cancel_button.grid(
            row = 0, column = 1, padx = 10, pady = 5,
            sticky = tkinter.E + tkinter.S)

        ''' Resizing '''
        self._options_window.rowconfigure(0, weight = 1)
        self._options_window.rowconfigure(1, weight = 1)
        self._options_window.rowconfigure(2, weight = 1)
        self._options_window.rowconfigure(3, weight = 1)
        self._options_window.rowconfigure(4, weight = 1)
        self._options_window.rowconfigure(5, weight = 1)
        self._options_window.rowconfigure(6, weight = 1)
        self._options_window.columnconfigure(0, weight = 1)
        self._options_window.columnconfigure(1, weight = 1)

        
        ''' Checking to see if the ok button was clicked and the returned values '''
        self._ok_clicked = False
        self._row_number = 0
        self._column_number = 0


    def get_row_number(self) -> int:
        return int(self._row_number)


    def get_column_number(self) -> int:
        return int(self._column_number)


    def get_first_player(self) -> str:
        return self.first_player.get()


    def get_win_con(self) -> str:
        return self.win_con.get()


    def _on_ok_clicked(self) -> None:
        ''' Checks the rows and columns using the gamelogic file '''
        check1 = othello_gamelogic.Othello.check_rows(self.row_number_entry.get())
        check2 = othello_gamelogic.Othello.check_columns(self.column_number_entry.get())

        if check1 is False or check2 is False:
            self.options_label.configure(text = 'Invalid Rows or Columns.\nMust be and even integer between 4-16.')
        elif check1 is True and check2 is True:
            self._ok_clicked = True
            self._row_number = self.row_number_entry.get()
            self._column_number = self.column_number_entry.get()
            self._options_window.destroy()


    def _on_cancel_clicked(self) -> None:
        self._options_window.destroy()


    def show(self) -> None:
        ''' Shows the window '''
        self._options_window.grab_set()
        self._options_window.wait_window()
