from tictactoe import player,actions,result,winner,terminal,utility,minimax,max_value,min_value


X = "X"
O = "O"
EMPTY = None



def main():
    # a = [[X,EMPTY,EMPTY],[EMPTY,O,EMPTY],[X,EMPTY,EMPTY]] board is important
    a = [[EMPTY,EMPTY,X],[EMPTY,X,EMPTY],[EMPTY,O,O]]
    res = minimax(a)
    print(res)

# def minimax(board):
#     """
#     Returns the optimal action for the current player on the board.
#     """
#     if terminal(board):
#         return None
#     current = player(board)
#     optimal = (0,0)
#     if current == X:
#         v = -10
#         for action in actions(board):
#             value = min_value(result(board,action))
#             if value > v:
#                 v = value
#                 optimal = action
#     if current == O:
#         v = 10
#         for action in actions(board):
#             value = max_value(result(board,action))
#             if value < v:
#                 v = value
#                 optimal = action
#     return optimal
#
#
# def max_value(board):
#     if terminal(board):
#         return utility(board)
#     v = -10
#     for action in actions(board):
#         v = max(v,min_value(result(board,action)))
#     return v
#
# def min_value(board):
#     if terminal(board):
#         return utility(board)
#     v = 10
#     for action in actions(board):
#         v = min(v,max_value(result(board,action)))
#     return v





if __name__ == "__main__":
    main()
