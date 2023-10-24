"""
Tic Tac Toe Player
"""

import math
import copy

X = "X"
O = "O"
EMPTY = None
LAX = []
LAO = []


def initial_state():
    """
    Returns starting state of the board.
    """
    return [[EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY]]

#recieve a state and return which player will play
#if it is empty, player return X, if X make a move, player return O
#the next to make a move will always be the one with less moves in the board
def player(board):
    """
    Returns player who has the next turn on a board.
    
    """
    counter_empty = 0
    counter_x = 0
    counter_o = 0
    
    for i in board:
        for j in i:
            if j == None:
                counter_empty += 1
            elif j == 'X':
                counter_x += 1
            elif j == 'O':
                counter_o += 1
    
    #if board empty, X starts
    if counter_empty == 9:
        return X
    #every time X makes a move, O is the next
    elif counter_x > counter_o:
        return O
    #every time O makes a move, X is the next
    elif counter_o == counter_x:
        return X


def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """
    actions = set()
    row = -1
    cell = -1
   
    for i in board:
        #incremet the row
        row += 1
        for j in i:
            #increment the cell
            cell +=1
            #if the there is a X or O do not add the cell incremental to the tupple
            if j == X or j == O:
                pass
            else:
                actions.add((row,cell))
            
            #reset counter
            if cell >= 2:
                cell = -1
  
    return actions
    #returns a tuple (i,j) 



def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    Recieve a board and one action, and return the move made by the action
    """
    """
    MISSING
    -If action is not a valid action for the board, your program should raise an exception.
    """
    #get the action and convert it to a list
    action_index = list(action)
    #create a copy of the board
    board2 = copy.deepcopy(board)
    #add the player's action in the board
    board2[action_index[0]][action_index[1]] = player(board2)
    
    return board2

    #returns a new board with the new action
    



def winner(board):
    """
    Returns the winner of the game, if there is one.
    """
    
    #CHECK ROW 1
    counterX = 0
    counterO = 0
    for i in board[0]:
        if i == "X":
            counterX += 1
            if counterX == 3:
                return X
        if i == "O":
            counterO += 1
            if counterO == 3:
                return O
     
    #CHECK ROW 2           
    if counterO == 3 or counterX == 3:
        pass
    else:  
        counterX = 0
        counterO = 0   
        for i in board[1]:
            if i == "X":
                counterX += 1
                if counterX == 3:
                    return X
            if i == "O":
                counterO += 1
                if counterO == 3:
                    return O
                    
    #CHECK ROW 3          
    if counterO == 3 or counterX == 3:
        pass
    else:  
        counterX = 0
        counterO = 0   
        for i in board[2]:
            if i == "X":
                counterX += 1
                if counterX == 3:
                    return X
            if i == "O":
                counterO += 1
                if counterO == 3:
                    return O
                    
    #CHECK CELL 1
    if board[0][0] == "X" and board[1][0] == "X" and board[2][0] == "X":
        return X
    if board[0][0] == "O" and board[1][0] == "O" and board[2][0] == "O":
        return O
        
    #CHECK CELL 2
    if board[0][1] == "X" and board[1][1] == "X" and board[2][1] == "X":
        return X
    if board[0][1] == "O" and board[1][1] == "O" and board[2][1] == "O":
        return O
        
    #CHECK CELL 3
    if board[0][2] == "X" and board[1][2] == "X" and board[2][2] == "X":
        return X
    if board[0][2] == "O" and board[1][2] == "O" and board[2][2] == "O":
        return O
        
        
    #CHECK DIAGNONAL 1
    if board[0][0] == "X" and board[1][1] == "X" and board[2][2] == "X":
        return X
    if board[0][0] == "O" and board[1][1] == "O" and board[2][2] == "O":
        return O
        
    #CHECK DIAGNONAL 2
    if board[0][2] == "X" and board[1][1] == "X" and board[2][0] == "X":
        return X
    if board[0][2] == "O" and board[1][1] == "O" and board[2][0] == "O":
        return O


def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """
    if winner(board) == "O" or winner(board) == "X":
        return True
    else:
        return False
    

def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """
    if winner(board) == "X":
        return 1
    if winner(board) == "O":
        return -1
    else:
        return 0

def maxvalue(board):
    v = -math.inf
    if terminal(board):
        return utility(board)
    
    else:
        for action in actions(board):
            v = max(v, minvalue(result(board, action))) 
            if utility(result(board, action)) == 1:
                print(result(board, action))
                LAX.append(action)
                break
        return v
    
def minvalue(board):
    v = math.inf
    if terminal(board):
        return utility(board)
    else:
        for action in actions(board):
           
            v = min(v, maxvalue(result(board, action)))
            if utility(result(board, action)) == -1:
                LAX.append(action)
                break           
           
                
        return v

def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    
    """
    if player(board) == X:
        print("X PLAYING")
        if maxvalue(board) == -1 or maxvalue(board) == 1:
        #get last move of max value (2, 0)
            print(LAX[-1])
            return LAX[-1]
        elif maxvalue(board) == math.inf:
        #get last move of max value (2, 0)
            print(LAX[-1])
            return LAX[-1]
        
    if player(board) == O:
        print("O PLAYING")
        if minvalue(board) == 1 or minvalue(board) == -1:
            #get last move of max value (2, 0)
            print(LAX[-1])
            return LAX[-1]
    
        elif minvalue(board) == -math.inf:
        #get last move of max value (2, 0)
            print(LAX[-1])
            return LAX[-1]
    
    
    print(maxvalue(board))   

    
boards1 = [[O, X, X],
            [EMPTY, X, O],
            [EMPTY, EMPTY, EMPTY]]
minimax(boards1)   


print(LAX)

 
