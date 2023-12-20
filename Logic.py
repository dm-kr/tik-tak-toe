import random
import copy


class Game:
    def __init__(self):
        self.board = [[" " for col in range(3)] for row in range(3)]
        self.current_turn = "X"
    
    def is_winner(self, moves=None):
        if moves == None:
            moves = self.board
        for row in range(3):
            if moves[row][0] == moves[row][1] == moves[row][2] != " ":
                return True
        
        for col in range(3):
            if moves[0][col] == moves[1][col] == moves[2][col] != " ":
                return True
        
        if moves[0][0] == moves[1][1] == moves[2][2] != " ":
            return True
        
        if moves[0][2] == moves[1][1] == moves[2][0] != " ":
            return True
        
        return False
       
    def get_potential_win(self):
        moves = copy.deepcopy(self.board)
        for i in range(3):
            for j in range(3):
                if moves[i][j] != " ":
                    continue
                moves[i][j] = "O"
                if self.is_winner(moves=moves):
                    return (i, j)
                moves[i][j] = "X"
                if self.is_winner(moves=moves):
                    return (i, j)
                moves[i][j] = " "
        return None
    
    def is_board_full(self):
        for row in self.board:
            for cell in row:
                if cell == " ":
                    return False
        return True
    
    def make_a_move_human(self, row, col):
        if self.board[row][col] == " ":
            self.board[row][col] = self.current_turn

        if self.is_winner():
            return self.current_turn
        elif self.is_board_full():
            return "draw"
        else:
            self.current_turn = "O" if self.current_turn == "X" else "X"
            return self.board
    
    def make_a_move_pc(self, row, col):
        self.board[row][col] = self.current_turn
        
        if self.is_winner():
            return "human"
        
        if self.is_board_full():
            return "draw"
        
        if self.board[1][1] == " ":
            self.board[1][1] = "O"
            return self.board
        
        cell = self.get_potential_win()
        if cell:
            self.board[cell[0]][cell[1]] = "O"
            return "pc" if self.is_winner() else self.board
        else:
            available_moves = []
            for row in range(3):
                for col in range(3):
                    if self.board[row][col] == " ":
                        available_moves.append((row, col))
            r, c = random.choice(available_moves)
            self.board[r][c] = "O"
            return "pc" if self.is_winner() else self.board
