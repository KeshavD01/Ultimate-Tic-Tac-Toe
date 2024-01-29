import tkinter as tk
from tkinter import messagebox
from SinglePlayerUltimateXO import SuperTicTacToe as SinglePlayerUltimate


class TicTacToe:
    def __init__(self):
        self.window = tk.Tk()
        self.window.title("Tic Tac Toe")
        self.current_player = 'X'
        self.board = [' ' for _ in range(9)]

        self.menu_frame = tk.Frame(self.window)
        self.menu_frame.pack()

        self.mode_label = tk.Label(self.menu_frame, text="Single Player Mode", font=('Comic Sans MS', 32))
        self.mode_label.grid(row=0, column=0, padx=5, pady=5)

        self.start_normal_button = tk.Button(self.menu_frame, text="Tic-Tac-Toe", font=('Comic Sans MS', 32), height=2, width=20,command=self.start_single_player_game)
        self.start_normal_button.grid(row=1, column=0, padx=5, pady=5)
        self.start_ultimate_button = tk.Button(self.menu_frame, text="Ultimate Tic-Tac-Toe", font=('Comic Sans MS', 32), height=2, width=20,command=self.start_singleplayer_ultimate)
        self.start_ultimate_button.grid(row=2, column=0, padx=5, pady=5)

        self.buttons = []

    def start_single_player_game(self):
        self.menu_frame.destroy()
        self.create_board()
        self.run_single_player_game()

    def start_singleplayer_ultimate(self):
        self.window.destroy()
        single_ultimate=SinglePlayerUltimate()

    def create_board(self):
        for i in range(3):
            for j in range(3):
                button = tk.Button(self.window, text='', font=('Comic Sans MS', 20, 'bold'), width=10, height=4,
                                   command=lambda row=i, col=j: self.on_click(row, col))
                button.grid(row=i, column=j)
                self.buttons.append(button)

    def on_click(self, row, col):
        index = 3 * row + col
        if self.board[index] == ' ':
            self.board[index] = self.current_player
            self.buttons[index].config(text=self.current_player)
            if self.check_winner():
                messagebox.showinfo("Tic Tac Toe", f"Player {self.current_player} wins!")
                self.reset_game()
            elif ' ' not in self.board:
                messagebox.showinfo("Tic Tac Toe", "It's a tie!")
                self.reset_game()
            else:
                self.switch_player()
                if self.current_player == 'O':
                    self.make_computer_move()

    def switch_player(self):
        self.current_player = 'O' if self.current_player == 'X' else 'X'

    def make_computer_move(self):
        if ' ' in self.board:
            index = self.minimax(self.board, 'O')['index']
            self.board[index] = 'O'
            self.buttons[index].config(text='O')
            if self.check_winner():
                messagebox.showinfo("Tic Tac Toe", "Player O wins!")
                self.reset_game()
            elif ' ' not in self.board:
                messagebox.showinfo("Tic Tac Toe", "It's a tie!")
                self.reset_game()
            else:
                self.switch_player()

    def reset_game(self):
        self.current_player = 'X'
        self.board = [' ' for _ in range(9)]
        for button in self.buttons:
            button.config(text='')

    def check_winner(self):
        winning_combinations = [(0, 1, 2), (3, 4, 5), (6, 7, 8), (0, 3, 6), (1, 4, 7), (2, 5, 8), (0, 4, 8), (2, 4, 6)]
        for combo in winning_combinations:
            if self.board[combo[0]] == self.board[combo[1]] == self.board[combo[2]] != ' ':
                return True
        return False

    def minimax(self, board, player):
        empty_spots = [i for i, spot in enumerate(board) if spot == ' ']

        if self.check_winner() and player == 'O':
            return {'score': -1}
        elif self.check_winner() and player == 'X':
            return {'score': 1}
        elif not empty_spots:
            return {'score': 0}

        moves = []
        for spot in empty_spots:
            move = {}
            move['index'] = spot
            board[spot] = player
            result = self.minimax(board, 'X' if player == 'O' else 'O')
            move['score'] = result['score']
            board[spot] = ' '
            moves.append(move)

        if player == 'O':
            best_move = max(moves, key=lambda x: x['score'])
        else:
            best_move = min(moves, key=lambda x: x['score'])

        return best_move

    def run_single_player_game(self):
        self.window.mainloop()


if __name__ == "__main__":
    game = TicTacToe()
    game.start_single_player_game()