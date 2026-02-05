
"""
You are given two integers m and n representing a 0-indexed m x n grid. 
You are also given two 2D integer arrays guards and walls where guards[i] = [rowi, coli] and walls[j] = [rowj, colj] --
 -- represent the positions of the ith guard and jth wall respectively.

A guard can see every cell in the four cardinal directions (north, east, south, or west) starting from their position unless obstructed by a wall or another guard. 
A cell is guarded if there is at least one guard that can see it.

"""

from typing import List
class Solution:
    def countUnguarded(self, m: int, n: int, guards: List[List[int]], walls: List[List[int]]) -> int:

        count = 0
        # there is no elegant solution other than brute force.
        # we should start out by creating the grid.
        grid = []
        for _ in range(m):
            grid.append([0 for _ in range(n)]) # zero is the unguarded position.

        # let's place the walls
        
        for wall in walls:
            grid[wall[0]][wall[1]] = 2 # two is a wall

        # let's place the guards.

        for guard in guards:
            grid[guard[0]][guard[1]] = 3
        
        # now a loop that properly marks the guarded cells by the guards.
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

        for i0, row in enumerate(grid):

            for i1, cell in enumerate(row):

                if cell == 3: # we hit a guard. then a loop should play
                    for direction in directions:
                        iy = i0
                        ix = i1
                        while True:
                            iy += direction[0]
                            ix += direction[1]
                            if not (0 <= iy < m and 0 <= ix < n): # it needed to be moved to a check after, since it would terminate at the border before.
                                break
                            if grid[iy][ix] > 1: # if it hits a guard or wall
                                break
                            grid[iy][ix] = 1 # the cell is now marked as guarded

        for row in grid:

            for cell in row:
                if cell == 0:
                    count += 1
        return count
                            

inp = Solution()

m = 4
n = 6
g = [[0,0],[1,1],[2,3]]
w = [[0,1],[2,2],[1,4]]

print(inp.countUnguarded(m,n,g,w))

[[3, 2, 0, 0, 0, 0], 
 [0, 3, 0, 0, 2, 0], 
 [0, 0, 2, 3, 0, 0], 
 [0, 0, 0, 0, 0, 0]]

[[3, 2, 0, 1, 0, 1], 
 [1, 3, 1, 1, 2, 1], 
 [1, 1, 2, 3, 1, 1], 
 [1, 1, 0, 1, 0, 0]]


[[3, 2, 0, 1, 0, 0], 
 [1, 3, 1, 1, 2, 0], 
 [0, 1, 2, 3, 1, 1], 
 [0, 1, 0, 1, 0, 0]]



