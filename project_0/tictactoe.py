"""
Tic Tac Toe Player
"""
import copy
import math

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

    countx=0
    counto=0

    for row in range(len(board)):
        for col in range(len(board[row])):
            if board[row][col] == X:
                countx+=1
            elif board[row][col] == O:
                counto+=1

    if countx > counto:
        return O
    else:
        return X


def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """
    actions = set()

    for row in range(len(board)):
        for col in range(len(board[row])):
            if board[row][col] == EMPTY:
                actions.add((row, col))

    return actions

def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """
    if action not in actions(board):
        raise Exception("Invalid action")
    
    row,col = action
    new_board =copy.deepcopy(board)
    new_board[row][col] = player(board)
    return new_board




def winOX(board):
    for row in range(len(board)):
        if board[row][0] == board[row][1] == board[row][2] == O and board[row][0] != EMPTY:
            return board[row][0]
        elif board[row][0] == board[row][1] == board[row][2] == X and board[row][0] != EMPTY:
            return board[row][0]
    for col in range(len(board[0])):
        if board[0][col] == board[1][col] == board[2][col] == O and board[0][col] != EMPTY:
            return board[0][col]
        elif board[0][col] == board[1][col] == board[2][col] == X and board[0][col] != EMPTY:
            return board[0][col]
    return None

def winD(board):
    if board[0][0] == board[1][1] == board[2][2] and board[0][0] != EMPTY:
        return board[0][0]
    if board[0][2] == board[1][1] == board[2][0] and board[0][2] != EMPTY:
        return board[0][2]
    return None

def winner(board):
    """
    Returns the winner of the game, if there is one.
    """
   
    if winOX(board) !=None:
          return winOX(board)
    
    elif winD(board) != None:
        return winD(board)
    
   
   
    
    return None
            
                
            
               
   

def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """

    if winner(board) == X or winner(board) == O or len(actions(board)) == 0:
        return True
    else:
        return False
    


def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """
    if winner(board) == X and winner(board) != None:
        return 1
    elif winner(board) == O and winner(board) != None:
        return -1
    else:
        return 0


def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """
    if terminal(board):
        return None
    if player(board) == X:
        best_score = -math.inf
        best_move=None
        for action in actions(board):
            v = mini(result(board, action))
            if  v > best_score:
                best_score = v
                best_move = action
        return best_move
    else:
        best_score = math.inf
        best_move=None
        for action in actions(board):
            v = maxi(result(board, action))
            if  v < best_score:  
                best_score = v
                best_move = action
        return best_move

def mini(board):
    if terminal(board):
        return utility(board)
    v = math.inf
    for action in actions(board):
        v = min(v, maxi(result(board, action)))
    return v

def maxi(board):
    if terminal(board):
        return utility(board)
    v = -math.inf
    for action in actions(board):
        v = max(v, mini(result(board, action)))
    return v