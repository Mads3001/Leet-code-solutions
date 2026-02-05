



from typing import List

# this creates an n * n matrix with 0-indexed all zeroes.
# we get a list of queries that makes two corners of a square, where we need to increment each element in the square by 1.
# that can be done multiple times. There can be up to 10.000 queries, so we might need something more effecient to apply the queries faster.
# we need the "2D Difference Array Technique". it creates a "dummy" 2D array, where only the corners are modified for each query.
# that makes each query 0(1). At last the middle of the corners are filled out. That vastly improves the time, so it is only a matter of the grid size (n*n) and queries (n)
# the final complexity is then only the fillin, which is at worst n * n, but only once.

class Solution:
    def rangeAddQueries(self, n: int, queries: List[List[int]]) -> List[List[int]]:

        dummy = [[0] * n for i in range(n)] # n*n grid

        for query in queries: # i think i fucked the queries up.
            dummy[query[0]][query[1]] += 1 # top left
            if query[2] + 1 < n:
                dummy[query[2] + 1][query[1]] -= 1 # bottom left
            if query[3] + 1 < n:
                dummy[query[0]][query[3] + 1] -= 1 # top right
            if query[2] + 1 < n and query[3] + 1 < n:
                dummy[query[2] + 1][query[3] + 1] += 1 # bottom right

            # this only adds to the top left corner and then the adjacent cell to the other corners.
        # now we need to fill the real values in.
        # We have decreased some of the values, because the way we fill in the cells take the values from the predecessor.
        # by applying the 1 early and the -1 later means the 1 will be added to every cell after the 1. When it hits the -1 it will proceed to apply the original 1 then -1 ---
        # --- to the rest. That way it can actually fill everything with just two passses of each cell. Once horisontal and then vertical.
        for r in range(n):
            for c in range(1, n): # the 1, is so they don't begin to take values from the back.
                dummy[r][c] += dummy[r][c - 1] # this fills it out for the rows.
        
        for c in range(n):
            for r in range(1, n):
                dummy[r][c] += dummy[r - 1][c] # this fills it out for the collumns
        
        return dummy
        

inp = Solution()

n = 3
q = [[1,1,2,2],[0,0,1,1]]

print(inp.rangeAddQueries(n,q))


# This builds off something similar, but with only a singular array.

# you get a singular array and need to add a value withing a certain range of the array.
# the query is list[value, start, stop]
class Solution:
    def rangeAddQueries(self, arr: List[int], queries: List[List[int]]) -> List[int]:
        
        dummy = [0 for i in range(len(arr))]
        for query in queries:
            dummy[query[1]] += query[0]
            dummy[query[2 + 1]] -= query[0]
        
        for i in range(1, len(arr)):
            dummy[i] += dummy[i - 1]
        
        for i, num in enumerate(dummy):
            arr[i] += num
        return arr
    # this is the solution for a 1D array. We just implement it sort of twice, when working with it in the other solution.


        