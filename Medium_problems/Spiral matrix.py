
# this time we need to disperse of a matrix into a spiral form.

def spiralOrder(self, matrix: list[list[int]]) -> list[int]:

    # let's make some bools to try and decide what direction the pattern is moving.
    up = False # it starts out by being false, since it should move down the first time it faces that question.
    reverse = False # it is straight the first time it is encountered.
    
    spiral_matrix = []
    # we must determine the size of the matrix
    rows = len(matrix)
    collumns = len(matrix[0])



    # the loops cut off the first element, so they don't overlap. Therefore the first element need to be appended manually.

    
    # we must make two loops. One that traverses vertically and one horisontally.
    r = 0 # the index of the current row that is worked on.
    c = 0 # the same but for collumn
    # there should be a while loop that is active, until the middle have been reached.
    r_rev = 0 # the reverse ones. They don't update at the same time
    c_rev = 0
    while len(spiral_matrix) < rows * collumns: # while there aren't the same number of elements.
    # i is negative, when moving in reverse
        if reverse:
            for i in range(c_rev + 2, collumns - c_rev): # it should start at the currently worked collumn. It should stop before it reaches the top that has already been counted.
                # the top length should then be 
                spiral_matrix.append(matrix[-r][-i]) # it is also the last list, when in reverse, since it is in the bottom.
            reverse = False
            c_rev += 1
            # the first reverse. It takes matrix[-1][-1] -> takes matrix[-1][-3] ()
        else:
            for i in range(c, collumns - c): 
                spiral_matrix.append(matrix[r][i]) # this starts at row 0 and appends all elements except the first.
            reverse = True # it is set, so the next time it is reverse
            # it takes matrix[0][0] -> matrix[0][3] the first time (grabs 3 numbers [2, 3, 4])
            c += 1
        
            
        if up:
            for i in range(r_rev + 1, rows - r_rev):
                spiral_matrix.append(matrix[-i][c - 1]) 
            up = False
            r_rev += 1
        else:
            for i in range(r + 1, rows - r): 
                spiral_matrix.append(matrix[i][-(c)]) # it is the last collumn, when traversing down.
            up = True
            # it takes matrix[1][-1] -> matrix[2][-1] the first times (grabs 2 numbers [8, 12])
            r += 1
    return spiral_matrix
"""
input = [[1,2,3,4],
         [5,6,7,8],
         [9,10,11,12]]
"""
input = [[1,2,9,9,3,4,5,1],
         [1,2,9,9,1,4,1,1],
         [1,10,9,9,3,4,5,1],
         [1,21,9,9,3,4,5,1],
         [1,2,9,3,3,4,3,3],
         [1,2,9,9,3,4,15,1]]

print(spiralOrder(0, input))

# my solution is not fast, but very memory effecient.


# this solution is fast. it makes some subfunctions that takes a certain amount of a row by using the specified details.
# There are four versions. it is a very elegant solution.
class Solution:
    def spiralOrder(self, matrix: list[list[int]]) -> list[int]:

        matrix_list = [number for row in matrix for number in row]
        
        rows = len(matrix)
        cols = len(matrix[0])

        if rows == 1:
            return matrix[0]

        skip_row_right = rows - 2
        skip_row_left = rows - 2

        output = []
        iteration = -1

        def top(matrix, iteration, cols, output):
            output += matrix[iteration][iteration : cols - iteration]

        def right(matrix, iteration, skip_row_right, output):

            for i in range(1 + iteration, skip_row_right - iteration + 1):
                output += [matrix[i][-1 - iteration]]
 
        def bottom(matrix, iteration, cols, output):
            output += reversed(matrix[-1 - iteration][iteration : cols - iteration])

        def left(matrix, iteration, skip_row_left, output):

            for i in range(skip_row_left - iteration, iteration, -1):
                output += [matrix[i][0 + iteration]]
        
        while len(output) < len(matrix_list):
            iteration += 1

            top(matrix, iteration, cols, output)

            if len(output) < len(matrix_list):
                right(matrix, iteration, skip_row_right, output)
            
            if len(output) < len(matrix_list):
                bottom(matrix, iteration, cols, output)
            
            if len(output) < len(matrix_list):
                left(matrix, iteration, skip_row_left, output)

        return output
    
# another beatiful solution is modifying the original array by popping.
# this just has a specific order it executes the removal of elements. Since the matrix also becomes smaller it automatically works without having to keep track of much.
# I wonder how much faster this is?

class Solution:
    def spiralOrder(self, matrix: list[list[int]]) -> list[int]:
        result = []

        while matrix:
            # Top row
            result += matrix.pop(0)

            # Right column
            if matrix and matrix[0]:
                for row in matrix:
                    result.append(row.pop())

            # Bottom row (reversed)
            if matrix:
                result += matrix.pop()[::-1]

            # Left column (bottom to top)
            if matrix and matrix[0]:
                for row in reversed(matrix):
                    result.append(row.pop(0))

        return result
# my first solution used less memory, but this was miles faster.


# my solution, but without comments. (I write wayyy to many comments normally)

def spiralOrder(self, matrix: list[list[int]]) -> list[int]:

    up = False 
    reverse = False
    
    spiral_matrix = []
    rows = len(matrix)
    collumns = len(matrix[0])

    r = 0 
    c = 0 

    c_rev = 0
    r_rev = 0
    while len(spiral_matrix) < rows * collumns: 
        if reverse:
            for i in range(c_rev + 2, collumns - c_rev):  
                spiral_matrix.append(matrix[-r][-i])
            reverse = False
            c_rev += 1

        else:
            for i in range(c, collumns - c): 
                spiral_matrix.append(matrix[r][i])
            reverse = True
            c += 1 
            
        if up:
            for i in range(r_rev + 1, rows - r_rev):
                spiral_matrix.append(matrix[-i][c - 1]) 
            up = False
            r_rev += 1
        else:
            for i in range(r + 1, rows - r): 
                spiral_matrix.append(matrix[i][-(c)])
            up = True
            r += 1
    
    return spiral_matrix





