#sudoku grid of size 9x9
grid = [
    [3, 0, 6, 5, 0, 8, 4, 0, 0],  
    [5, 2, 0, 0, 0, 0, 0, 0, 0],  
    [0, 8, 7, 0, 0, 0, 0, 3, 1],  
    [0, 0, 3, 0, 1, 0, 0, 8, 0],  
    [9, 0, 0, 8, 6, 3, 0, 0, 5],  
    [0, 5, 0, 0, 9, 0, 6, 0, 0],  
    [1, 3, 0, 0, 0, 0, 2, 5, 0],  
    [0, 0, 0, 0, 0, 0, 0, 7, 4],  
    [0, 0, 5, 2, 0, 6, 3, 0, 0] 
]
#Find an empty position in the box
def find_empty_box(board): # to find an empty box in the grid 
    for i in range(len(board)):      
        for j in range(len(board[0])):
            if(board[i][j]==0):
                return (i,j)  #row,column returned as a tuple
    return None


# To Print the board in sudoku style and for beter styling 
def print_board(board):
    for i in range(len(board)):
        if(i%3==0 and i!=0):            # To print a dashed/dotted line after every three rows of board
            print("- - - - - - - - - - -")
        for j in range(len(board[0])):
            if(j%3==0 and j!=0):      # To print a line/margin after every three elements to show a 3x3 box
                print("|",end = " ")
            if j == 8:
                print(board[i][j])
            else:
                print(str(board[i][j]) + " ", end="")


# To Cehck if the number placed at an empty box is valid or not 
def validate_prediction(board,num,pos):  #here pos is a tuple of (row,column)
    # Checking in the row 
    for i in range(len(board[0])):
        if board[pos[0]][i] == num and pos[1]!=i:
            return False
    
    #Checking in the column 
    for i in range(len(board[0])):
        if board[i][pos[1]] == num and pos[0] !=1 :
            return False

    #Checking in 3x3 box 
    box_x = pos[1] // 3  #To determine the box 
    box_y = pos[0] // 3

    for i in range(box_y * 3 , box_y*3 + 3):
        for j in range(box_x * 3, box_x*3 + 3):
            if board[i][j]==num and (i,j)!=pos :
                return False
    
    #Once checked in row,column and 3x3 box, num is valid choice for that box thus return true
    return True

#Solver using backtracking 
def solve(board):
    find_box = find_empty_box(board)
    if not find_box:            #checking if all boxes are empty then stopping the algo
        return True
    else :
        row , col = find_box  #otherwise find an empty postion 
    
    #Placing 1..9 in found empty box and validating it 
    for i in range(1,10):
        if validate_prediction(board,i,(row,col)):
            board[row][col] = i

            if solve(board):    #Recursive call to solve next empty box 
                return True

            board[row][col] = 0         # If false is returned in the recurse call then we replcae current place with zero
    
    #Last exit condition in case the recent value is not a valid option  
    return False

print_board(grid)
print("Solving.....")
solve(grid)
print_board(grid)