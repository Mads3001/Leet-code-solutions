
# we get an array and we can apply one operation to a subarray, which consists of strictly decreasing values.
# That subarray will be set to zero and is one operation. We one operation for each of those subarrays.
# a subarray breaks, when the values begin to increase again. Thus, we can increase the amount of operations each time the following value in the array is greater than the previous


# I was wrong. The smallest value in that subarray is turned into zero. For that reason, zero can't be in the subarray.


from typing import List
class Solution:
    def minOperations(self, nums: List[int]) -> int:
        count = 0
        # we should start out by creating a queue from the smallest value to the largest.
        queue = list(set(nums))
        queue.sort(reverse=True) # we progressively pop an element until empty.

        if queue[-1] == 0:
            queue.pop()

        l = len(nums)
        while queue: # while not empty
            i = 0
            spotted_0 = True
            lowest = queue.pop()
            while i < l:
                # the count only goes up, if there has been a zero between the instances of the minimum value.
                if nums[i] == 0: # the order fucked it up, since the check was after the original value was set to zero.
                    spotted_0 = True

                if nums[i] == lowest:
                    nums[i] = 0
                    print(nums)
                    if spotted_0:
                        count += 1
                        spotted_0 = False

                i += 1
        return count
            
# it works very well, but may time out for very large sets with many unique values.
# working by storing the unique subarrays and the amount of each subarray might be better for larger sets of data.
# the current loop complexity is exponential.

n = [1,2,1,2,1,2]

inp = Solution()

print(inp.minOperations(n))


# I was wrong, and the original solution (which was wrong) was actually something along the lines of the correct solution.
# when we iterate over the numbers we can from there already see, if the number needs an operation to get rid off or if it has already been removed by a higher value.
# we then need to create a stack that keeps track of the numbers. A larger number can turn another number into 0. That consumes the number and costs an operation.

class Solution:
    def minOperations(self, nums: List[int]) -> int:
        count = 0 # amount of operations
        stack = []
        for num in nums:
            # if the stack exists (numbers that can turn num into zero), then it can turn num into zero and every element under that.
            while stack and stack[-1] > num:
                stack.pop()
            # it just skips, if num is zero
            if num == 0:
                continue # this skips directly to the next num in nums and skips the rest of the code for this iteration.
            if not stack or stack[-1] < num: # if it is greater than anything seen before or the stack is empty (nothing can be used to pop the current num)
                # then it will always take an operation to pop it. (the operation can also be used to pop another number)
                # the stack will always have a singular value left at last. That is the maximum value.
                count += 1
                stack.append(num)
        return count


        





