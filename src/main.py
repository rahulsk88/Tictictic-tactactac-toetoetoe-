## How should we start this?
## First define a simple board
## The board is a collection of 9 TicTacToe games
## So we must first define the smaller tictactoes

## To define the smaller tictactoes:
## We start with a simple class that defines these games
## The Larger game needs to setup these initialise these smaller tictactoes and control the overall game logic. But these inside tictactoes must have their own logics
 
## The tictactoes need to first initialise a basic structure:
    ## TODO: Define Board - This should be a list of lists? and we should set conditions for Win and Draw
    ## TODO: Define Players
    ## TODO: Define Playable Actions
    ## TODO: Define Win Conditions
    ## TODO: 


## Board = [[], [], []]
## set all to 0
class TicTacToe:
    def __init__(self):
        self._board = [[0, 0, 0],
                       [0, 0, 0], 
                       [0, 0, 0]] 
        self._valid_actions = [] # list of tuples containing the indices to populate the board. 

        self._player = 0

        self._game_over = False

    def _actions(self):
        if self._game_over:
            self._valid_actions = []
        else: 
            for i in self._board:
                for j in i:
                    self._valid_actions.append((i, j))
        
    def _turn(self):
        if self._player:
            self._actions()  ## make a note of all the actions and then allow the player to choose a specific one? How do they chose? 
            # Action
            self._player = 0
        else: 
            self._actions()
            self._player = 1

    def _game_status(self, action):
        ## Check _player, and then check whether the game has ended. 
        self.action = action # Should be the last played indice
        
         

        

        
        
