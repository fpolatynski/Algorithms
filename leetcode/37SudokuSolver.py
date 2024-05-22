from typing import List


def solveSudoku(board: List[List[str]]) -> None:
    """
    Do not return anything, modify board in-place instead.
    """
    # Select unassigned value
    board = backtracking(board)

def backtracking(board):
    # Select unassigned value
    var = select_value(board)
    
    # If sudoku is compleadted return
    if not var:
        return board
    
    # iterate over possibles values
    for value in domain_values():
        # Check if  value is valid and update board
        if is_valid_number(board, value, var):
            board[var[0]][var[1]] = value
            result = backtracking(board)
            if result != None:
                return result
        board[var[0]][var[1]] = "."
    return None
                               
def domain_values():
    for x in range(9):
        yield str(x+1)

def select_value(board):
    for i, r in enumerate(board):
        for j, c in enumerate(r):
            if c == ".":
                return i, j
    return None

def is_valid_number(board, number, place):
    # Check chunk
    X = place[0] % 3
    Y = place[1] % 3
    for x in range(place[0] - X, place[0] + 3 - X):
        for y in range(place[1] - Y, place[1] + 3 - Y):
            if board[x][y] == number:
                return False
            
    # check row
    for x in range(9):
        if board[x][place[1]] == number:
            return False
    
    # Check columns
    for y in range(9):
        if board[place[0]][y] == number:
            return False
    
    return True

board = [["5","3",".",".","7",".",".",".","."],["6",".",".","1","9","5",".",".","."],[".","9","8",".",".",".",".","6","."],["8",".",".",".","6",".",".",".","3"],["4",".",".","8",".","3",".",".","1"],["7",".",".",".","2",".",".",".","6"],[".","6",".",".",".",".","2","8","."],[".",".",".","4","1","9",".",".","5"],[".",".",".",".","8",".",".","7","9"]]
print(backtracking(board))
    
            