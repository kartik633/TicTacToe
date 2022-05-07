"""
Tic Tac Toe Player
"""

import math
import copy

X = "X"
O = "O"
EMPTY = None


def initial_state():
    """
    Returns starting state of the board.
    """
    return [[EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY]]


def player(board):
    """
    Returns player who has the next turn on a board.
    """
    counter = 0
    for row in board:
        for value in row:
            if value == X or value == O:
                counter = counter+1
    if (counter%2) == 0:
        return X
    else:
        return O



def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """
    actions_list = set()
    for i in range(0,3):
        for j in range(0,3):
            if board[i][j] == EMPTY:
                actions_list.add((i,j))
    return actions_list



def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """
    if board[action[0]][action[1]] != EMPTY:
        raise NameError('Not a valid move!')
    board_copy = copy.deepcopy(board)
    value = player(board_copy)
    board_copy[ action[0] ][ action[1] ] = value
    return board_copy


def winner(board):
    """
    Returns the winner of the game, if there is one.
    """
    for each in board:
        if each[0] == each[1] and each[1] == each[2]:
            if each[0] != EMPTY:
                value = each[0]
                return value
    for i in range(0,3):
        if board[0][i] == board[1][i] and board[1][i] == board[2][i]:
            if board[0][i] != EMPTY:
                value = board[0][i]
                return value
    if board[0][0] == board[1][1] and board[1][1] == board[2][2]:
        if board[0][0] != EMPTY:
            value = board[0][0]
            return value
    if board[0][2] == board[1][1] and board[1][1] == board[2][0]:
        if board[0][2] != EMPTY:
            value = board[0][2]
            return value
    return None


def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """
    value = winner(board)
    if value != None:
        return True
    for row in board:
        for each in row:
            if each == EMPTY:
                return False
    return True


def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """
    value = winner(board)
    if value == X:
        return 1
    elif value == O:
        return -1
    else:
        return 0


def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """
    if terminal(board):
        return None
    current = player(board)
    optimal = (0,0)
    if current == X:
        v = -10
        for action in actions(board):
            value = min_value(result(board,action))
            if value > v:
                v = value
                optimal = action
    if current == O:
        v = 10
        for action in actions(board):
            value = max_value(result(board,action))
            if value < v:
                v = value
                optimal = action
    return optimal


def max_value(board):
    if terminal(board):
        return utility(board)
    v = -10
    for action in actions(board):
        value = min_value(result(board,action))
        if value > v:
            v = value
    return v

def min_value(board):
    if terminal(board):
        return utility(board)
    v = 10
    for action in actions(board):
        v = min(v,max_value(result(board,action)))
    return v
