import tkinter as tk
from tkinter import messagebox
import random

class SuperTicTacToe:
    def __init__(self):
        self.window = tk.Tk()
        self.window.title("Super Tic Tac Toe")

        self.supergrid = [[None for _ in range(3)] for _ in range(3)]
        self.current_player = 'X'
        self.current_supergrid = None

        self.create_supergrid()
        self.run_game()

    def create_supergrid(self):
        for i in range(3):
            for j in range(3):
                frame = tk.Frame(self.window, width=200, height=200, highlightthickness=2, highlightbackground="black")
                frame.grid(row=i, column=j, padx=2, pady=2)

                subgrid = [[None for _ in range(3)] for _ in range(3)]
                for row in range(3):
                    for col in range(3):
                        button = tk.Button(frame, text='', font=('Comic Sans MS', 10, 'bold'), width=5, height=3,
                                           command=lambda r=row, c=col, s_i=i, s_j=j: self.on_click(r, c, s_i, s_j))
                        button.grid(row=row, column=col, padx=1, pady=1)
                        subgrid[row][col] = button

                self.supergrid[i][j] = subgrid

    def on_click(self, row, col, supergrid_row, supergrid_col):
        if self.current_supergrid is None or (supergrid_row, supergrid_col) == self.current_supergrid:
            button = self.supergrid[supergrid_row][supergrid_col][row][col]

            if button['text'] == '':
                button['text'] = self.current_player

                if self.check_small_win(supergrid_row, supergrid_col):
                    messagebox.showinfo("Super Tic Tac Toe", f"Player {self.current_player} wins SuperSquare {supergrid_row}-{supergrid_col}!")
                    self.reset_game()
                elif self.is_supergrid_full():
                    messagebox.showinfo("Super Tic Tac Toe", "The game is a draw!")
                    self.reset_game()
                else:
                    self.update_current_supergrid(row, col)
                    self.switch_player()

                    # Highlight the new active super square
                    self.highlight_active_supergrid()

                    # Check if it's AI's turn
                    if self.current_player == 'O':
                        self.ai_move()

    def update_current_supergrid(self, row, col):
        if self.current_supergrid is not None:
            i, j = self.current_supergrid
            frame = self.window.grid_slaves(row=i, column=j)[0]
            frame.config(highlightbackground="black")

        self.current_supergrid = (row, col)

        if self.isSuperSquareFull(row, col):
            self.current_supergrid = None

    def switch_player(self):
        self.current_player = 'O' if self.current_player == 'X' else 'X'

    def reset_game(self):
        self.current_player = 'X'
        self.current_supergrid = None
        for i in range(3):
            for j in range(3):
                for row in range(3):
                    for col in range(3):
                        self.supergrid[i][j][row][col]['text'] = ''

    def check_small_win(self, supergrid_row, supergrid_col):
        subgrid = self.supergrid[supergrid_row][supergrid_col]
        for i in range(3):
            if self.check_tic_tac_toe(subgrid[i][0]['text'], subgrid[i][1]['text'], subgrid[i][2]['text']):
                return True
            if self.check_tic_tac_toe(subgrid[0][i]['text'], subgrid[1][i]['text'], subgrid[2][i]['text']):
                return True
        if self.check_tic_tac_toe(subgrid[0][0]['text'], subgrid[1][1]['text'], subgrid[2][2]['text']):
            return True
        if self.check_tic_tac_toe(subgrid[0][2]['text'], subgrid[1][1]['text'], subgrid[2][0]['text']):
            return True
        return False

    def check_tic_tac_toe(self, a, b, c):
        return a == b == c != ''

    def isSuperSquareFull(self, supergrid_row, supergrid_col):
        subgrid = self.supergrid[supergrid_row][supergrid_col]
        for row in range(3):
            for col in range(3):
                if subgrid[row][col]['text'] == '':
                    return False
        return True

    def is_supergrid_full(self):
        for i in range(3):
            for j in range(3):
                if not self.isSuperSquareFull(i, j):
                    return False
        return True

    def ai_move(self):
        supergrid_row, supergrid_col = self.current_supergrid
        subgrid = self.supergrid[supergrid_row][supergrid_col]

        empty_buttons = [(row, col) for row in range(3) for col in range(3) if subgrid[row][col]['text'] == '']
        if empty_buttons:
            ai_row, ai_col = random.choice(empty_buttons)
            subgrid[ai_row][ai_col]['text'] = 'O'
            if self.check_small_win(supergrid_row, supergrid_col):
                messagebox.showinfo("Super Tic Tac Toe", "Player O wins SuperSquare {}-{}!".format(supergrid_row, supergrid_col))
                self.reset_game()
            elif self.is_supergrid_full():
                messagebox.showinfo("Super Tic Tac Toe", "The game is a draw!")
                self.reset_game()
            else:
                self.update_current_supergrid(ai_row, ai_col)
                self.switch_player()

                self.highlight_active_supergrid()

    def highlight_active_supergrid(self):
        if self.current_supergrid is not None:
            i, j = self.current_supergrid
            frame = self.window.grid_slaves(row=i, column=j)[0]
            frame.config(highlightbackground="Dark Red")

    def run_game(self):
        self.window.mainloop()

if __name__ == "__main__":
    game = SuperTicTacToe()