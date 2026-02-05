
# the input is an array of numbers
# the output should be the maximum sum possible with the amount of elements being divisible by k.
# this problem can be solved with the help of a prefix sum
from typing import List
class Solution:
    def maxSubarraySum(self, nums: List[int], k: int) -> int:
        l = len(nums)
        pre = [0] * l # this is the prefix sum
        # we just find the max by sliding over the array
        highest = float('-inf')

        pre[0] = nums[0]
        for i, num in enumerate(nums[1:], 1): # this fills in the prefix sum
            pre[i] = pre[i - 1] + num
        
        # we need to figure out the lengths possible.
        lengths = [k]
        while lengths[-1] <= l - k:
            lengths.append(lengths[-1] + k)
        print(lengths, pre)

        # this tries each length
        for length in lengths:
            i_f = length - 1 # the starting index with length 2 should be 1.
            highest = max(highest, pre[i_f]) # sometimes the first elements grant the highest sum. In that case we don't subtract anything.
            
            i_f += 1 # now we reach a number where we need to subtract the first.

            while i_f < l: # l is the amount, so the highest index is one less.
                highest = max(highest, pre[i_f] - pre[i_f - length]) #e.g. the i_f is 2 and the length is two. Now the value subtracted is the first element
                i_f += 1
        return highest
    
inp = Solution()
n = [1,2]
k = 1
print(inp.maxSubarraySum(n,k))

# it doesn't quite work, when the biggest sum is the first part, but without subtracting the first element.
# there might also be some problems, if it is the last one.

# this works, but there is a more optimized algorithm called kadanes algorithm. It uses something true for a certain dataset to calculate it faster.
# my approach is by comparison rather naive, since it is O(N*l) where l is calculated based on k and the length.

# My approach timed out, so time to write the solution with kadanes algorithm

class Solution:
    def maxSubarraySum(self, nums: List[int], k: int) -> int:
        n = len(nums)

        # Running prefix sum (Kadane-style)
        prefSum = 0

        # Track min prefix sum for each modulo group (size k)
        # Ensures subarray length is divisible by k
        minSoFar = [0 if i == 0 else float("inf") for i in range(k)]

        # Store maximum subarray sum ending at each position
        # Only valid when length % k == 0
        subMax = [float("-inf")] * (n + 1)

        # Track overall maximum
        maxSum = float("-inf")

        for i in range(1, n + 1):
            # Update running prefix sum
            prefSum += nums[i - 1]
            mod = i % k

            # Calculate max subarray ending at i with length divisible by k
            # By comparing with positions having same modulo
            if minSoFar[mod] != float("inf"):
                subMax[i] = prefSum - minSoFar[mod]
                maxSum = max(maxSum, subMax[i])

            # Update minimum prefix sum for this modulo group
            minSoFar[mod] = min(minSoFar[mod], prefSum)

        return maxSum
        
        
# that way we keep track of the prefix sum and the minimum possible subarray for each index.
# the maximum subarray is the difference between the minimum and the prefix sum.
# it works a bit differently, when k is larger than 1.
# then we keep track of how many minimum possible is the same in sequence. When it doesn't change, then it means the current subarray is growing.
# Each time the value is the same minimum possible the length of the growing subarray is increased by 1.
# we can then check for certain lengths of subarrays and their value.


# the completely optimized version is:
import sys
class Solution:
    def maxSubarraySum(self, nums: List[int], k: int) -> int:
        prefSum = 0
        subMax = -sys.maxsize
        minSoFar = [sys.maxsize] * k
        minSoFar[(k - 1) % k] = 0

        for i, v in enumerate(nums):
            prefSum += v
            subMax = max(subMax, prefSum - minSoFar[i % k])
            minSoFar[i % k] = min(minSoFar[i % k], prefSum)

        return subMax

# the fastest method uses the same, but with some other ways of deciding the max, which is faster:

from math import inf

class Solution:
    def maxSubarraySum(self, nums: List[int], k: int) -> int:
        least_pre = [inf] * k
        least_pre[-1] = 0
        prefix_sum = 0
        max_sum = -inf
        for i, num in enumerate(nums):
            prefix_sum += num
            mod = i % k
            old_pre = least_pre[mod]
            sub_sum = prefix_sum - old_pre
            if max_sum < sub_sum:
                max_sum = sub_sum
            if old_pre > prefix_sum:
                least_pre[mod] = prefix_sum
        return max_sum