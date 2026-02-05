
# we meed to take a grid of lists and return all the lists combined, but in a diagonal order.

# we just need to do diagonal traversing

from typing import List

def findDiagonalOrder(self, mat: list[list[int]]) -> list[int]:

    # we need to find the rows and collumns.
    rows = len(mat)
    collumns = len(mat[0])
    diagonals = {} # we create a hash map with a list of all the values in a diagonal
    diagonal_list = []
    diag_num = collumns + rows - 1 # number of diagonals
    # the first element is mat[0][0]
    # the loop should then traverse to mat[0][1] -> mat[1][0] -> mat[2][0] -> mat[1][1] -> mat[0][2]
    # we must exploit, that the sum of the indices are the same as the number in the string.
    # we just create a loop that puts all the diagonals into hashmap. All the even diagonals should be reversed before getting inserted into the return list.

    for r in range(rows):
        for c in range(collumns):
            if (r + c) not in diagonals:
                diagonals[r + c] = []
            diagonals[r + c].append(mat[r][c]) # this will create a huge library with all the elements.
    # the library is created, then we just need to stitch together the return list.
    for d in range(diag_num):
        if d & 1 == 0: # if the first bit is 0 (the number is even), then the list needs to be reversed before being added to the diagonal list.
            diagonals[d].reverse()
        diagonal_list.extend(diagonals[d])
    return diagonal_list

# I think it should be around medium speed, but definitely not memory effective.
# other people that solved with less memory only stored one diagonal at a time and appended it before reseting the diagonal. 

input = [[1,2,3],
         [4,5,6],
         [7,8,9]]

print(findDiagonalOrder(0,input))


# that solution looked like this
class Solution:
    def findDiagonalOrder(self, mat: List[List[int]]) -> List[int]:
        m, n = len(mat), len(mat[0])
        result, inter = [], []
        for d in range(m + n - 1):
            r, c = 0 if d < n else d - n + 1, d if d < n else n - 1
            inter.clear()
            while r < m and c >= 0:
                inter.append(mat[r][c])
                r += 1
                c -= 1
            if d % 2 == 0:
                result.extend(inter[::-1])
            else:
                result.extend(inter)
        return result