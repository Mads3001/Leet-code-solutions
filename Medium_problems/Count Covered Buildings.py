
# a building is covered, if there are a building in each direction in the x-y plan adjacent to it.

# we can make a list of each row in the x or y plan.
# there is somehow a an O(N) solution. That can may be done, by some sort of counting, where the edge is the only ones not counted.
# we just need to find the edges of each axis. 

from typing import List
class Solution:
    def countCoveredBuildings(self, n: int, buildings: List[List[int]]) -> int:
        count = 0
        edgesx = {}
        edgesy = {}
        # have both x and y edges.
        # we should register the highest and lowest x edge for a given value for y. And the same for y.
        for building in buildings:
            if building[0] not in edgesy: # this marks the y-value edges at a given x-value
                edgesy[building[0]] = [building[1], building[1]] # left is the lowest edge. Right is the greates. (low, high)
            else:
                edgesy[building[0]][1] = max(edgesy[building[0]][1], building[1]) # reassigns the greatest edge, if new value is greater.
                edgesy[building[0]][0] = min(edgesy[building[0]][0], building[1]) # same for the lowest edge.

            if building[1] not in edgesx: # this marks the x-value edges at a given y-value
                edgesx[building[1]] = [building[0], building[0]] # (low, high)
            else:
                edgesx[building[1]][1] = max(edgesx[building[1]][1], building[0])
                edgesx[building[1]][0] = min(edgesx[building[1]][0], building[0])
        # now there should be data for the highest and lowest values for x and y in a particular collumn or row.

        for building in buildings:
            if (edgesy[building[0]][0] < building[1] < edgesy[building[0]][1] and 
                edgesx[building[1]][0] < building[0] < edgesx[building[1]][1]):
                count += 1
        return count

b = [[1,2],[2,2],[3,2],[2,1],[2,3]]
b = [[1,1],[1,2],[2,1],[2,2]]
b = [[57,91],[13,88],[58,65],[25,96],[56,74],[35,72],[50,36],[96,33],[24,26],[80,58],[44,93],[13,35],[6,68],[86,24],[94,7],[45,87],[17,16],[76,65],[95,100],[72,43],[29,54],[68,70],[50,86],[15,9],[53,57],[22,14],[40,84],[22,32],[1,76],[65,24],[89,58],[38,34],[83,84],[7,46],[96,23],[19,84],[40,15],[6,22],[60,57],[54,23],[92,7],[4,77],[66,70],[50,37],[19,86],[81,79],[42,97],[38,84],[32,98],[92,64],[32,43],[78,19],[85,67],[4,24],[24,57],[33,60],[45,34],[45,98],[33,78],[81,72],[73,68],[49,13],[95,19],[65,48],[37,66],[5,70],[38,49],[60,79],[17,29],[56,54],[30,44],[29,12],[40,21],[72,83],[26,40],[95,39],[88,55],[53,97],[64,60],[13,36],[7,29],[84,32],[37,36],[77,47],[36,12],[27,18],[65,75],[77,40],[29,64],[60,42],[20,70],[34,17],[31,27],[37,77],[5,72],[25,57],[2,73],[23,41],[5,35],[5,44]]

inp = Solution()
print(inp.countCoveredBuildings(3, b))


# the code has many lookups, so caching/unpacking values may be wise.
# alone by caching and unpacking values the overhead for lookup is removed, by assigning better pointers.
# the performance is doubled (runtime is halved) by those changes.
from typing import List

class Solution:
    def countCoveredBuildings(self, n: int, buildings: List[List[int]]) -> int:
        count = 0
        edgesx = {}
        edgesy = {}

        for x, y in buildings:
            ey = edgesy.get(x)
            if ey is None:
                edgesy[x] = [y, y]
            else:
                if y > ey[1]:
                    ey[1] = y
                if y < ey[0]:
                    ey[0] = y

            ex = edgesx.get(y)
            if ex is None:
                edgesx[y] = [x, x]
            else:
                if x > ex[1]:
                    ex[1] = x
                if x < ex[0]:
                    ex[0] = x

        for x, y in buildings:
            ey = edgesy[x]
            ex = edgesx[y]
            if ey[0] < y < ey[1] and ex[0] < x < ex[1]:
                count += 1

        return count



# an ultra optimized solution doesn't actually need a dictionary, but can suffice with a simple array to keep track of the values.

class Solution:
    def countCoveredBuildings(self, n: int, buildings: List[List[int]]) -> int:
        xMax, yMax=[0]*(n+1), [0]*(n+1)
        xMin, yMin=[1<<31]*(n+1), [1<<31]*(n+1)

        for x, y in buildings:
            xMin[y]=min(xMin[y], x)
            xMax[y]=max(xMax[y], x)
            yMin[x]=min(yMin[x], y)
            yMax[x]=max(yMax[x], y)

        cnt=0
        for x, y in buildings:
            coverX=(xMin[y]<x & x<xMax[y])
            coverY=(yMin[x]<y & y<yMax[x])
            cnt+=(coverX & coverY)
        return cnt



