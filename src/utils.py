import numpy as np


def check_win(board, last_played):
    row = last_played[0]
    col = last_played[1]

    ## Check if abs of the row sum is 3
    if np.abs(np.sum(board[row])) == 3:
        return True
    if np.abs(np.sum(board[:, col])) == 3:
        return True
    if np.abs(np.sum(np.diag(board))) == 3:
        return True
    if np.abs(np.sum(np.fliplr(board).diagonal())) ==3:
        return True
    else:
        False

## Think about a non-numpy solution but this should be okay for now. 