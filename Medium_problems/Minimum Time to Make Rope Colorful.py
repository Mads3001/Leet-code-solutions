
# The input is two arrays. One for the baloon colors. And one for the remove time for each balloon.

from typing import List
class Solution:
    def minCost(self, colors: str, neededTime: List[int]) -> int:

        # let's do a two pointer approach.
        all_time = 0

        i = 1
        consecutive_same = 0
        l = len(colors)
        while i < l:
            
            if colors[i] == colors[i-1]:
                consecutive_same += 1
            else:
                if consecutive_same:
                    time = sum(neededTime[_] for _ in range(i - consecutive_same - 1, i)) - max(neededTime[_] for _ in range(i - consecutive_same - 1, i))
                    all_time += time
                consecutive_same = 0
            i += 1
        
        if consecutive_same:
                    time = min(neededTime[_] for _ in range(i- consecutive_same - 1, i))  
                    all_time += time
        return all_time         

inp = Solution()

c = "abaac"
n = [1,2,3,4,5]

print(inp.minCost(c,n))

# it begins to become cluttered.

# i'll try a simpler two pointer approach.


class Solution:
    def minCost(self, colors: str, neededTime: List[int]) -> int:
         

        all_time = 0

        i_front = 0
        i_back = 0
        prev = ""
        l = len(colors)
        while i_front < l:
            if colors[i_front] == colors[i_back]:
                i_front += 1
            else:
                if i_front > i_back:
                    time = sum(neededTime[i_back:i_front]) - max(neededTime[i_back:i_front])
                    all_time += time
                i_back = i_front
        if i_front > i_back:
                    time = sum(neededTime[i_back:i_front]) - max(neededTime[i_back:i_front])
                    all_time += time
        return all_time

# the summing and taking the max is costly. Instead taking it in steps is better.
class Solution:
    def minCost(self, colors: str, neededTime: List[int]) -> int:
        total_time, curr_max_time = 0, 0

        for i in range(len(colors)):
            if i > 0 and colors[i] != colors[i - 1]:
                curr_max_time = 0
            total_time += min(curr_max_time, neededTime[i])
            curr_max_time = max(curr_max_time, neededTime[i])

        return total_time