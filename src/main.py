from utils import *
import numpy as np

class TicTacToe:
    def __init__(self):
        self._board = np.array(
            [[0, 0, 0],
             [0, 0, 0], 
             [0, 0, 0]])
        self._valid_actions = [] 
        self._player = 0
        self._game_over = False
        self._last_played = None

    def _actions(self):
        self._valid_actions = []
        actions = np.where(self._board == 0)
        print()
        for i in range(len(actions[0])):
            self._valid_actions.append((actions[0][i], actions[1][i]))

    def _update_board(self, row = None, col= None, player = None):     
        if (row == None) or (col == None):
            row = input("Enter Row number: ")
            col = input("Enter Col number: ")
            row = int(row)
            col = int(col)
            
        attempt = (row, col)
        
        if attempt in self._valid_actions:
            invalid = False
        else:
            print("Invalid Option, Try Again!")
            invalid = True
        
        while invalid:
            row = input("Enter Row number: ")
            col = input("Enter Col number: ")

            row = int(row)
            col = int(col)

            attempt = (row, col)
            if attempt in self._valid_actions:
                invalid = False
            else:
                print("Invalid Option, Try Again!")
                invalid = True
            
        self._last_played = (row, col)

        if player != None:
            self._player = player

        if self._player == 0:
            self._board[row, col] = 1
        if self._player == 1:
            self._board[row, col] = -1
        
        
        
    def _turn(self):
        self._actions()
        self._update_board()
        self._check_win()
        self._check_draw()
        self._actions()

        if self._player:
            self._player = 0
        else:
            self._player = 1
        
        
    def _check_win(self):

        #if self._last_played is None:
        #    self. False


        row = self._last_played[0]
        col = self._last_played[1]

        ## Check if abs of the row sum is 3
        if np.abs(np.sum(self._board[row])) == 3:
            self.win = True
            self._game_over = True
        if np.abs(np.sum(self._board[:, col])) == 3:
            self.win = True
            self._game_over = True
        if np.abs(np.sum(np.diag(self._board))) == 3:
            self.win = True
            self._game_over = True
        if np.abs(np.sum(np.fliplr(self._board).diagonal())) == 3:
            self.win = True
            self._game_over = True
        else: 
            self.win = False
    
    def _check_draw(self):
        self._check_win()
        if (not self.win) and (self._valid_actions == []):
            self.draw = True
            self._game_over = True
        else: 
            self.draw = False

class ult_tictactoe:
    def __init__(self):
        self._board  = {}

        for i in [(0,0), (0,1), (0,2), (1,0), (1,1), (1,2), (2,0), (2,1), (2,2)]:
            self._board[i] = TicTacToe()
        self._player = 0
        self.game_over = False
        self.key = None
    
    def _game_condition(self):
        row_grid = self.key[0]
        col_grid = self.key[1]

        if ((self._board[(row_grid, 0)]._game_over) & (self._board[(row_grid, 1)]._game_over) & 
            (self._board[(row_grid, 2)]._game_over))| ((self._board[(0, col_grid)]._game_over) & 
            (self._board[(1, col_grid)]._game_over) & (self._board[(2, col_grid)]._game_over)):
            self.game_over = True
        
        if ((row_grid == 1) | (row_grid == 1))  and not (row_grid == col_grid):
            
            self.game_over = False
        elif ((self._board[(0, 0)]._game_over) & (self._board[(1, 1)]._game_over) & 
            (self._board[(2, 2)]._game_over))| ((self._board[(0, 2)]._game_over) & 
            (self._board[(1, 1)]._game_over) & (self._board[(2, 0)]._game_over)):
            self.game_over = True
            
    def _first_turn(self):

            row_square = input("Enter Board Row Number: ")
            col_square = input("Enter Board Col Number: ")

            row_square = int(row_square)
            col_square = int(col_square)

            self.key = (row_square, col_square)
            self._board[self.key]._actions()
            print(f"Possible Actions: {self._board[self.key]._valid_actions}")

            
            row_input = input("Enter Row number: ")
            col_input = input("Enter Col number: ")

            row_input = int(row_input)
            col_input = int(col_input)


            self._board[self.key]._update_board(row = row_input, col = col_input, player = self._player) 
            self._board[self.key]._check_draw()
            self._board[self.key]._check_win()
            self.key = self._board[self.key]._last_played
            self._game_condition()
            self._player = 1
    
    def turn(self):
        self._visualise_board()
        if not self._board[self.key]._game_over: 

            print(f"Current Board ID {self.key}")
            self._board[self.key]._actions()
            print(f"Possible Actions: {self._board[self.key]._valid_actions}")

            ## Player Move:
            row_input = input("Please Input a Row:")
            col_input = input("Please Input a Col:")

            row_input = int(row_input)
            col_input = int(col_input)

            ## Move Update:

            self._board[self.key]._update_board(row = row_input, col = col_input, player = self._player) 
            self._board[self.key]._check_draw()
            self._board[self.key]._check_win()
            
            ## TO ensure there are no errors:
            self.key = self._board[self.key]._last_played
            self._game_condition()
            
        ## Need to add logic for the other type of moves that can be played where you pick your location and tile
        else: 

            row_square = input("Enter Board Row Number: ")
            col_square = input("Enter Board Col Number: ")

            row_square = int(row_square)
            col_square = int(col_square)

            self.key = (row_square, col_square)
            
            row_input = input("Enter Row number: ")
            col_input = input("Enter Col number: ")

            row_input = int(row_input)
            col_input = int(col_input)

            ## Move Update:
            self._board[self.key]._actions()
            self._board[self.key]._update_board(row = row_input, col = col_input, player = self._player) 
            self._board[self.key]._check_draw()
            self._board[self.key]._check_win()

            self.key = self._board[self.key]._last_played
            self._game_condition()
    
    def _visualise_board(self):
        print("", self._board[(0, 0)]._board[0, :], "|", self._board[(0, 1)]._board[0, :], "|", self._board[(0, 2)]._board[0, :],"\n",
              self._board[(0, 0)]._board[1, :], "|", self._board[(0, 1)]._board[1, :], "|", self._board[(0, 2)]._board[1, :],"\n",
              self._board[(0, 0)]._board[2, :], "|", self._board[(0, 1)]._board[2, :], "|", self._board[(0, 2)]._board[2, :],"\n",
              "--------|---------|--------- \n",
              self._board[(1, 0)]._board[0, :], "|", self._board[(1, 1)]._board[0, :], "|", self._board[(1, 2)]._board[0, :],"\n",
              self._board[(1, 0)]._board[1, :], "|", self._board[(1, 1)]._board[1, :], "|", self._board[(1, 2)]._board[1, :],"\n",
              self._board[(1, 0)]._board[2, :], "|", self._board[(1, 1)]._board[2, :], "|", self._board[(1, 2)]._board[2, :],"\n",
               "--------|---------|--------- \n",
              self._board[(2, 0)]._board[0, :], "|", self._board[(2, 1)]._board[0, :], "|", self._board[(2, 2)]._board[0, :],"\n",
              self._board[(2, 0)]._board[1, :], "|", self._board[(2, 1)]._board[1, :], "|", self._board[(2, 2)]._board[1, :],"\n",
              self._board[(2, 0)]._board[2, :], "|", self._board[(2, 1)]._board[2, :], "|", self._board[(2, 2)]._board[2, :],"\n",)


    def play_game(self):
        self._first_turn()
        
        while not self.game_over:
            self.turn()
            if self._player == 1:
                self._player = 0 
            elif self._player == 0:
                self._player = 1
        
        print(f"Player {self._player} has won!")


hi = ult_tictactoe()
hi.play_game()
        

    

