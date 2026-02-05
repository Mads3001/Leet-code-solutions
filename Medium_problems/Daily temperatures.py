
# the input is an array of temperatures over some days. The output need to be the amount of days you have to wait for each given day to find a day --
# -- which is hotter than the previous.

# I can make an O(N) solution by going over the array twice.
# The first pass marks each time the day is hotter than the day before.
# No, that wouldn't work, since it can be hotter than the day before, but not hot enough.
# We need to create a stack of temperatures and their location. That way we can maybe search with binary search to find the smallest value next greater value.

# We need to create a monotoic stack. A decreasing one. That means, each time an element is inserted, then each element smaller than that is popped.

# We iterate from the back of the array this way.

from typing import List
class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        ans = [] # it will need to be reversed before returned.
        stack = []
        for i, temp in enumerate(temperatures[::-1], 1): # it starts at 1
            while stack and stack[-1][0] <= temp: # elements less or equal to the current one is popped.
                stack.pop()
            if stack:
                 # if the stack remains, then the top element is the next greatest element. We have access to that elements index, so we just calculate the difference --
                 # -- and add that to the answer array
                ans.append(i - stack[-1][1])
            else:
                ans.append(0)
            stack.append((temp, i))

        return ans[::-1]

# this creates a tuple, but it might be faster, if it is only using index.




# by only using index it frees up some memory. The time is not that great though.
class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        ans = []
        stack = []
        l = len(temperatures)
        for i in range(l - 1, -1, -1): # it starts at 1
            while stack and stack[-1][0] <= temperatures[i]: # elements less or equal to the current one is popped.
                stack.pop()
            if stack:

                ans.append(i - stack[-1][1])
            else:
                ans.append(0)
            stack.append((temperatures[i], i))

        return ans[::-1]


# the faster solution incoorporates the index better without tuples.
# by having the top of the stack as an index we can just plug that index into the temperatures and go from there instead.
# no need for tuples.

class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []
        l = len(temperatures)
        ans = [0] * l
        for i in range(l - 1, -1, -1): # it starts at 1
            current_temp = temperatures[i]
            while stack and temperatures[stack[-1]] <= current_temp: # elements less or equal to the current one is popped.
                stack.pop()
            if stack:
                ans[i] = stack[-1] - i
            stack.append(i)
        return ans
# We can also try to build the ans instead of having prefilled zeroes.


class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []
        l = len(temperatures)
        ans = []
        for i in range(l - 1, -1, -1): # it starts at 1
            current_temp = temperatures[i]
            while stack and temperatures[stack[-1]] <= current_temp: # elements less or equal to the current one is popped.
                stack.pop()
            if stack:
                ans.append(stack[-1] - i)
            else:
                ans.append(0)
            stack.append(i)
        return ans[::-1]

# this is around the same speed as the good solution, since it also uses a better way of keeping track of the stack. It is random though, if it is around that speed.
# it is the most memory efficient yet.
# Storing the temperatures[i] might be an idead to limit the calls.

