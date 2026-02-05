

# A grid of input should be converted to a diagonal grid. the bottom half of the diagonal grid (including the middle) should be sorted from largest to smallest.
# The upper half of the diagonal grid should be sorted from smallest to largest.
# the grid should then be put back as it was before, and the sorting should only take the diagonal grid into account

def sortMatrix(self, grid: list[list[int]]) -> list[list[int]]:
    # the size of the grid should first be assesed
    row = len(grid) # this is how many rows there are

    # the diagonal grid should now be filled into the diagonal lists
    # each point in the grid has a value of (row-col). Each point on the same diagonal list have the same value for (row-col).
    for i in range(row): 
        """this will iterate over how many rows there are in the grid. This is very useful, 
         because this will mark the start of all the diagonals under under and including the middle """
        # this:  """ """ is a multiline string, but can also just be a multiline comment, when it is not set for anything
        diag_list = [grid[i + j][j] for j in range(row - i)] # the list will have a constant value for i, but will increase j. j marks the collumn.
        # the code is structured, so it will create a new temporary list each time.
        diag_list.sort(reverse = True)
        for j in range(row - i):
            grid[i + j][j] = diag_list[j] # this will paste in the temporary diagonal list correctly on the grid
    # this code has now sorted the bottom half of the grid
    
    for i in range(1, row):
        diag_list = [grid[j][j + i] for j in range(row - i)] # this time it will now iterate over the rows instead of collumns.
        diag_list.sort() # the list is now over the top half of the grid
        for j in range(row - i):
            grid[j][i + j] = diag_list [j]
    return grid
    
grid = [[1,7,3,5],
        [9,8,2,5],
        [4,5,6,6],
        [4,5,6,6]]

print(sortMatrix(0, grid))

# it will return
new_grid = [[8, 2, 3, 5],
            [9, 6, 6, 5], 
            [5, 6, 6, 7], 
            [4, 4, 5, 1]]

# very smart stuff. It was a solution by the internet, that i sort of get, but don't really. It makes sense and works.