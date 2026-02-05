
# this code receives a target array. It should output the minimum amount of actions needed to create target array from an all zero array.
# an action is increasing any number of adjacent indices by 1.

# instead of constructing we can just deconcstruct. We find the first instance of the maximum and remove 1 from that index and the adjacent indices.

from typing import List

class Solution:
    def minNumberOperations(self, target: List[int]) -> int:
        l = len(target)
        end = [0 for i in range(l)] # this is for comparison purposes.
        steps = 0

        while target != end:

            next_step = max(target)

            for i, num in enumerate(target):
                if num == next_step:
                    while i <l and num == target[i]: # this loops subtracts from the adjacent indices
                        target[i] -= 1
                        i += 1
                    break
            steps += 1
        return steps # this should be a simple solution.

# it works but is too slow.


class Solution:
    def minNumberOperations(self, target: List[int]) -> int:
        l = len(target)
        steps = 0

        while set(target) != {0}:
            next_step = max(target)
            i = target.index(next_step)
            while target[i] == next_step:

                target[i] -= 1
                if i == l - 1:
                    break
                i += 1
            print(target)
            print(next_step)
            steps += 1
        return steps # this should be a simple solution.

inp = Solution()
t = [1,2,3,2,1]
print(inp.minNumberOperations(t))

# still times out.


# maybe we should do it off of how many extra steps the next element adds


class Solution:
    def minNumberOperations(self, target: List[int]) -> int:
        steps = 0
        # the base amount of steps is the minimum value
        # the extra steps comes, when there's a hill
        last_base = 0 # last base gets updated, if the num is less than hill top.
        for num in target:
            if num > last_base:
                steps += num - last_base
            last_base = num
        return steps
