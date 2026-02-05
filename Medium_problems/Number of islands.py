
# I need to implement breadth first search into this problem.
# we get a grid with numbers where 1 is land and 0 is water. Everything out of the matrix is water.
grid = [
  ["1","1","1","1","0"],
  ["1","1","0","1","0"],
  ["1","1","0","0","0"],
  ["0","0","0","0","0"]]
# the grid has 1 island. I don't know how to implement the breadth first search, because I don't know what it'll do.

# breadth first search start at a certain point and then pushes adjacent nodes to a queue in waves until everything have been traversed. 
# it does that by keeping track of the visisted nodes. That code can mark an island as visited, but what good does it do in this scenario?

# maybe the code should start a breadth first search to mark an island each time we find a one that aren't on the visisted list.

# the workflow would be:
# 1. finds a 1 that isn't in the visited list.
# 2. the whole island is marked with breadth first search and put in the visited list. 
# 3. an island is added for each breadth first search and that island's 1's are visisted, so they can't trigger another search.
# 4. the iterator moves forward and tries to find another 1 that isn't in the visisted list.

from collections import deque

# i need the deque to put up a queue for the 

class Solution:
    

    def numIslands(self, grid: list[list[str]]) -> int:

        self.visited = set()
        self.rows = len(grid) - 1
        self.columns = len(grid[0]) - 1
        self.queue = deque()
        self.grid = grid

        count = 0

        for row in range(self.rows + 1):

            for column in range(self.collumns + 1):
                if grid[row][column] == "1" and (row, column) not in self.visited:
                    self.queue.append((row, column)) # tuple for speed reasons and they don't need to be mutable
                    self.visited.add((row, column))
                    while self.queue: # while the queue is not empty
                        self.bfs(self.queue[0])
                        self.queue.popleft() # the current object is then removed from the queue.

                    # each time the bfs loop is triggered, then an island have been spotted.
                    count += 1
                    print(self.visited)
        return count

    def bfs(self, point: list[int]):
        # this should just be the code that adds to the queue
        # the residual points should be checked and maybe added to the queue.

        if 0 < point[0]: # there is enough space to try the row before (up)
            if (point[0] - 1, point[1]) not in self.visited: # check if it has been visited before.
                if self.grid[point[0] - 1][point[1]] == "1": # if the grid has land, then it is added to the queue.
                    self.queue.append((point[0] - 1, point[1])) # the new coordinates are added to the queue.
                    self.visited.add((point[0] - 1, point[1])) # they are also put into visited, so the other nodes can't make duplicates


        if point[0] < self.rows: # there is enough space to try the row after (down)
            if (point[0] + 1, point[1]) not in self.visited: 
                if self.grid[point[0] + 1][point[1]] == "1": 
                    self.queue.append((point[0] + 1, point[1]))
                    self.visited.add((point[0] + 1, point[1])) 

        if 0 < point[1]: # there is enough space to try the collumn before (left)
            if (point[0], point[1] - 1) not in self.visited: 
                if self.grid[point[0]][point[1] - 1] == "1": 
                    self.queue.append((point[0], point[1] - 1)) 
                    self.visited.add((point[0], point[1] - 1)) 

        if point[1] < self.collumns: # there is enough space to try the collumn after (right)
            if (point[0], point[1] + 1) not in self.visited: 
                if self.grid[point[0]][point[1] + 1] == "1": 
                    self.queue.append((point[0], point[1] + 1)) 
                    self.visited.add((point[0], point[1] + 1)) 

        
inp = Solution()
p = [["1","1","0","0","0"],
     ["1","1","0","0","0"],
     ["0","0","1","0","0"],
     ["0","0","0","1","1"]]
print(inp.numIslands(p))


        
# the bfs should add the surrounding elements to the queue. The element will only be added, if it is a 1 and within the grid.
# it is then added to a queue. the element is added by its coordinates.


# an optimized version is shown now:

from typing import List
from collections import deque

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid or not grid[0]: # faster return, if the grid is empty.
            return 0

        rows, cols = len(grid), len(grid[0])
        visited = set()
        count = 0

        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)] # preset directions, so adding to queue is smoother.

        def bfs(r, c): # instead of creating it as a method we just use it in the first method.
            # that is faster, since we can just keep using local scope variables instead of it being kept track of between methods.
            queue = deque() # creates a new dequeue each time bfs is triggered. Since islands can't be up against each other, then it still works.
            queue.append((r, c))
            visited.add((r, c))
            while queue:
                row, col = queue.popleft()
                for dr, dc in directions:
                    nr, nc = row + dr, col + dc
                    if (0 <= nr < rows and 0 <= nc < cols and
                        grid[nr][nc] == "1" and (nr, nc) not in visited): # this is a longer check instead of multiple if statements.
                        queue.append((nr, nc))
                        visited.add((nr, nc))

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == "1" and (r, c) not in visited:
                    bfs(r, c)
                    count += 1

        return count
    



# BFS is more memory intensive, so DFS (depth first search) could also be better, since it can be implemented recursively, which can be faster with python
# the problem arises, if the explored island is very big, since the recursive depth could become a problem.

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid:
            return 0
        
        def dfs(i, j):
            if i < 0 or i >= len(grid) or j < 0 or j >= len(grid[0]) or grid[i][j] != '1':
                return
            grid[i][j] = '0'  # mark as visited
            dfs(i+1, j)
            dfs(i-1, j)
            dfs(i, j+1)
            dfs(i, j-1)
        
        num_islands = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == '1':
                    num_islands += 1
                    dfs(i, j) # this will erase all surrounding 1 to 0's. This is also a good approach.
        
        return num_islands
    


# my implementation with dfs
# dfs uses a stack order, where last in - first out is the order instead of first in - first out.

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid:
            return 0
        visited = set()
        count = 0
        rows = len(grid)
        columns = len(grid[0])

        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        def dfs(row, column):
            stack = []
            stack.append((row, column))
            visited.add((row, column))
            while stack:
                r, c = stack.pop()
                for dr, dc in directions:
                    newr = r + dr
                    newc = c + dc
                    if (0 <= newr < rows and 0 <= newc < columns and
                        grid[newr][newc] == "1" and (newr, newc) not in visited):
                        stack.append((newr, newc))
                        visited.add((newr, newc))
        for r in range(rows):
            for c in range(columns):
                if grid[r][c] == "1" and (r, c) not in visited:
                    dfs(r, c)
                    count += 1
        return count
                    





