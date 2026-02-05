
# the code should start at an element being zero. The pointer will then move either left or right until it hits an element greater than zero.
# the hit element will decrement by 1 and change the direction of the pointer.


from typing import List

class Solution:
    def countValidSelections(self, nums: List[int]) -> int:

        # let's write two loops. One that starts right and one that starts left.

        count = 0 # this is the amount of starts that lead to a victory. (when all elements have been decremented to 0 before the process stops.)

        starting_points = []
        l = len(nums)

        for i, num in enumerate(nums):
            if num == 0:
                starting_points.append(i) # add valid starting points to a list.

        
        for start in starting_points: # this for loop chooses the starting points. two loop should then simulate the process.
            
            board = nums[:]
            i = start
            move = 1
            while -1 < i < l: # the bounds. 
                if board[i] > 0:
                    board[i] -= 1
                    move = -move # flips the direction
                i += move
            if sum(board) == 0:
                count += 1
            # the loop stops, when i is out of bounds. If it is succesful, then it should only contain zeroes (one singular value).
            # the loop should then run again, but starting with moving left instead of right.

            board = nums[:]
            i = start
            move = -1 # starts moving left
            while -1 < i < l: # the bounds. 
                if board[i] > 0:
                    board[i] -= 1
                    move = -move # flips the direction
                i += move
            if sum(board) == 0:
                count += 1
        return count

inp = Solution()
g = [1,0,2,0,3]
print(inp.countValidSelections(g))


# a faster solution could just check the sum to the right and to the left of the zero. They must be equal or have a difference of 1. Else it isn't a valid solution.



class Solution:
    def countValidSelections(self, nums: List[int]) -> int:

        count = 0
        left = 0
        right = sum(nums)
        for num in nums:
            right -= num
            if num == 0: # each time this is found, it checks for the sum to the right and left.
                # if the difference of the sides are 1, then 1 start move can win. if the difference is zero, then both work.
                diff = abs(left - right)
                if diff == 0:
                    count += 2
                if diff == 1:
                    count += 1
            left += num


# I could also try to sum the right and left on the way. That may be faster due to it being built-in.

class Solution:
    def countValidSelections(self, nums: List[int]) -> int:

        count = 0
        for i, num in enumerate(nums):
            if num == 0: # each time this is found, it checks for the sum to the right and left.
                # if the difference of the sides are 1, then 1 start move can win. if the difference is zero, then both work.
                diff = abs(sum(nums[:i]) - sum(nums[i:]))
                if diff == 0:
                    count += 2
                if diff == 1:
                    count += 1

# this is actually faster even though it does redundant summation. It just might be due to the sum() being compiled, so it is faster.