import tkinter as tk
from tkinter import messagebox
from SinglePlayerXO import TicTacToe as SinglePlayerGame
from MultiPlayerXO import TicTacToe as TwoPlayerGame


class MainMenu:
    
    def __init__(self):
        self.window = tk.Tk()
        self.window.title("Tic Tac Toe Menu")

        self.menu_frame = tk.Frame(self.window)
        self.menu_frame.pack()

        self.title_label = tk.Label(self.menu_frame, text="Tic Tac Toe Menu", font=('Comic Sans MS', 32))
        self.title_label.grid(row=0, column=0, padx=5, pady=5)

        self.single_player_button = tk.Button(self.menu_frame, text="Single Player", font=('Comic Sans MS', 20),
                                              height=2, width=20, command=self.start_single_player_game)
        self.single_player_button.grid(row=1, column=0, padx=5, pady=5)

        self.two_player_button = tk.Button(self.menu_frame, text="Two Player", font=('Comic Sans MS', 20),
                                           height=2, width=20, command=self.start_two_player_game)
        self.two_player_button.grid(row=2, column=0, padx=5, pady=5)

        

    def start_single_player_game(self):
        self.window.destroy()
        single_player_game = SinglePlayerGame()

    def start_two_player_game(self):
        self.window.destroy()
        two_player_game = TwoPlayerGame()

    def run_menu(self):
        self.window.mainloop()

if __name__ == "__main__":
    menu = MainMenu()
    menu.run_menu()
    



