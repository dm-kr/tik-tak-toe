import tkinter as tk
from tkinter import messagebox
import Logic
import ChildWindow

class UI:
    def __init__(self):
        self.game_menu = tk.Tk()
        self.game_menu.configure(bg="#232a2f")
        self.game_menu.geometry("250x250")
        self.game_menu.title("Tik Tak Toe")
        title = tk.Label(self.game_menu, text="Tik Tak Toe", background="#232a2f", fg="white")
        singleplayer = tk.Button(self.game_menu, text="Single Player", background="#4e7da5",
                                width=30, height=2, command=lambda x="pc": self.create_board(x))
        multiplayer = tk.Button(self.game_menu, text="Multi Player", background="#4e7da5",
                                width=30, height=2, command=lambda x="human": self.create_board(x))
        title.pack(side="top", pady="10px")
        singleplayer.pack(side="top", pady="10px")
        multiplayer.pack(side="top", pady="10px")
        self.game = Logic.Game()
        self.board: list
    
    def create_board(self, opponent):
        self.game_menu.withdraw()
        self.board_window = ChildWindow.ChildWindow(self.game_menu)
        self.board_window.configure(bg="#232a2f")
        self.board_window.geometry("400x400")
        self.board_window.resizable(width=False, height=False)
        self.board_window.title(f"Tik Tak Toe")
        
        board = []
        for row in range(3):
            button_row = []
            for col in range(3):
                button = tk.Button(self.board_window, text=" ", width=10, height=5)
                if opponent == "pc":
                    button.configure(command=lambda r=row, c=col, o=opponent: self.move(r, c, o))
                else:
                    button.configure(command=lambda r=row, c=col, o=opponent: self.move(r, c, o))
                button.grid(row=row, column=col)
                button_row.append(button)
            board.append(button_row)
        self.board = board
        self.board_window.mainloop()
    
    def move(self, row, col, opponent):
        if opponent == "pc":
            move_result = self.game.make_a_move_pc(row, col)
            if move_result in ["human", "pc", "draw"]:
                if move_result == "draw":
                    msg = "draw!"
                else:
                    msg = f"{move_result} wins!"
                self.board_window.withdraw()
                msb = messagebox.Message(type="ok", title="Game over", message=msg)
                msb.show()
                self.board_window.destroy()
            else:
                for row in range(3):
                    for col in range(3):
                        if self.board[row][col]["text"] != move_result[row][col]:
                            self.board[row][col]["text"] = move_result[row][col]
                            self.board[row][col]["state"] = "disabled"
        else:
            move_result = self.game.make_a_move_human(row, col)
            if move_result in ["X", "O", "draw"]:
                if move_result == "draw":
                    msg = "draw!"
                else:
                    msg = f"{move_result} wins!"
                self.board_window.withdraw()
                msb = messagebox.Message(type="ok", title="Game over", message=msg)
                msb.show()
                self.board_window.destroy()
            else:
                for row in range(3):
                    for col in range(3):
                        if self.board[row][col]["text"] != move_result[row][col]:
                            self.board[row][col]["text"] = move_result[row][col]
                            self.board[row][col]["state"] = "disabled" 
    
    def start(self):
        self.game_menu.mainloop()