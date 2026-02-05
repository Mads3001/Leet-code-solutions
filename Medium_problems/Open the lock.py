
# this code needs to unlock a combination lock with 4 digits. It should return the minimum amount of actions to unlock the lock.
# the twist is, that there are some specific combinations where the lock will get stuck.
# The code must find the best solution while avoiding getting stuck.
# -1 should be returned, if there is no valid solution.


# I can write a bruteforce solution that tries every single combination. The upper limit will just be incredibly large.
# it will not be very effecient, probably run out of time and eat memory like nothing you've seen before.


from typing import List
from collections import deque

class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:
        

        if "0000" in deadends:
            return -1
        # deadends should just be added to visited.
        # since we need to keep track of steps I'll use a dictionary (hashmap)
        visited = {}

        for deadend in deadends:
            visited[deadend] = 0 # they are just marked as already explored. I will then use the key value to store the steps.

        queue = deque()

        queue.append((list("0000"), 0)) # the starting position
        visited["0000"] = 0
        
        
        directions = ((0,1), (1,1), (2,1), (3,1),
                      (0,-1), (1,-1), (2,-1), (3,-1)) # directions will be stored in tuples. the first one is the index of the number that will change.
        

        while target not in visited:
            if not queue: # if empty 
                return -1
            
            for direction in directions:
                combination = queue[0][0][:] # this takes a deep copy of the list, since it will be modified.
                combination[direction[0]] = str((int(combination[direction[0]]) + direction[1] + 10) % 10) # takes the correct index and applies either +1 or -1 to the value as an int.
                # then it takes mod 10, since the code lock works like that.
                combi_key =  "".join(combination)
                if combi_key not in visited:
                    visited[combi_key] = 1 + int(queue[0][1]) # this assigns the amount of steps it needs to take to reach that specific sequence.
                    queue.append((list(combi_key), visited[combi_key])) # it is now added to the queue.
            queue.popleft()

        # if the while loop has ceased, then the target has been found.
        print(visited)
        return visited[target]

dd = ["0201","0101","0102","1212","2002"]
t = "0202"

inp = Solution()
print(inp.openLock(dd,t))
