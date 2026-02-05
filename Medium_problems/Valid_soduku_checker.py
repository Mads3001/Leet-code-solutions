# A grid for a soduko is the input
# the code will need to assess, if the current start of the sudoku is valid. It doesn't need to be solvable.

# an input could be: board = 
""" 
[["5","3",".",".","7",".",".",".","."]
,["6",".",".","1","9","5",".",".","."]
,[".","9","8",".",".",".",".","6","."]
,["8",".",".",".","6",".",".",".","3"]
,["4",".",".","8",".","3",".",".","1"]
,["7",".",".",".","2",".",".",".","6"]
,[".","6",".",".",".",".","2","8","."]
,[".",".",".","4","1","9",".",".","5"]
,[".",".",".",".","8",".",".","7","9"]] """

# the code will need to check every horisontal line, vertical line and each little 3x3 square.
# we can make a hash map for everything that needs to be checked.

def isValidSudoku(self, board: list[list[str]]) -> bool:

    
    for index, hor_list in enumerate(board): # this takes each horisonal line in the grid and feeds one horisontal line at a time to the inner loop.
        temp_dict = {}
        temp_dict["."] = -9 # this is a safeguard, because there can be multiple ".". Any other duplicate will activate a false.
        for value in board[index]:
            
            temp_dict[value] = 1 + temp_dict.get(value, 0) # the amount of a certain value will get put into a dictionary.

            if temp_dict[value] > 1: # if there is multiple of the same value in the horisontal line, then the soduko is not valid.
                return False


    for index, vert_list in enumerate(board): # now it is time for the vertical lines.
        temp_dict = {}
        temp_dict["."] = -9

        for inner_index, value in enumerate(board[index]): # this gives inner index the values from 0 to 8. Now it will take the character from the same vertical line. 
            # it is iterating, so the the numbers will be taken from the next horisontal line.

            temp_dict[board[inner_index][index]] = 1 + temp_dict.get(board[inner_index][index], 0)
        
        if temp_dict [board[inner_index][index]] > 1:
            return False

    # now we need to check for the squares

    # I will try to make a function that checks a square.

    # I will make a list from a 3x3 square of values.
    square_list = []

    for x in range(3): # this loops extends it to the three horisontal squares.
        for n in range(3): # this loop extends it to the three left squares (row).
            square = []
            for i in range(3): # this for loop will create a list of a 3x3 square and append it to the square list.
                square.append(board[0 + 3 * n][0 + i + 3 * x])
                square.append(board[1 + 3 * n][0 + i + 3 * x])
                square.append(board[2 + 3 * n][0 + i + 3 * x])
            square_list.append(square)

    # now we have a list of all the squares. We can now check for duplicates in each square.

    for square in square_list: # The square is a list.
        temp_dict = {}
        temp_dict["."] = -9
        for value in square:
            temp_dict[value] = 1 + temp_dict.get(value, 0)
            
            if temp_dict[value] > 1:
                return False
    return True


        

board = [ [".",".","4",".",".",".","6","3","."]
         ,[".",".",".",".",".",".",".",".","."]
         ,["5",".",".",".",".",".",".","9","."]
         ,[".",".",".","5","6",".",".",".","."]
         ,["4",".","3",".",".",".",".",".","1"]
         ,[".",".",".","7",".",".",".",".","."]
         ,[".",".",".","5",".",".",".",".","."]
         ,[".",".",".",".",".",".",".",".","."]
         ,[".",".",".",".",".",".",".",".","."]]
print(isValidSudoku(0, board))



# the better solution by the internet

class Solution:
    def isValidSudoku(self, board: list[list[str]]) -> bool:
        rows = [[False] * 9 for _ in range(9)] # those create nine lists (one for each row) of nine elements (for each value) that are all false for all rows.
        cols = [[False] * 9 for _ in range(9)]
        boxes = [[False] * 9 for _ in range(9)]

        for i in range(9):
            for j in range(9):
                if board[i][j] != '.': # when the cell is not empty it gets triggered
                    num = ord(board[i][j]) - ord('1')
                    boxIndex = (i // 3) * 3 + (j // 3)
                    if rows[i][num] or cols[j][num] or boxes[boxIndex][num]: # this is a check, if the value has already been seen. If any is true, then it is invalid
                        return False
                    rows[i][num] = cols[j][num] = boxes[boxIndex][num] = True # If it isn't seen before, then i and j marks the row and collumn and boxindex, which box it is in.
                    # the number "num" is marked as seen in that row, collumn and box. num can be 9 different values, but if the same value is seen again, then it will be true, and false is returned
        return True