
# the input is an array of numbers. The output should be the maximum sum of the numbers, which are divisible by 3.

from typing import List

class Solution:
    def maxSumDivThree(self, nums: List[int]) -> int:

        nums.sort()

        # we start out by taking the sum of everything.
        ans = sum(nums)
        ans2 = ans
        rest = ans % 3
        rest2 = rest
        le = len(nums)
        i = 0
        l = 0
        while rest and i < le: # this loop experiments with taking only cases where the rest is 1 for the number. (removing up to two numbers)
            l = nums[i] % 3
            if l == 1:
                ans -= nums[i]
                rest = (rest - (nums[i] % 3)) % 3
            i += 1
        if rest:
            ans = 0
        
        i = 0
        while rest2 and i < le: # this loop epxeriments with the rest as 2 and ultimately only removing one number.
            l = nums[i] % 3
            if l == 2:
                ans2 -= nums[i]
                rest2 = (rest2 - (nums[i] % 3)) % 3
            i += 1
        if rest2:
            ans2 = 0
        return max(ans, ans2)

# I didn't write the proper dynamic programming solution, but just turned it into a questions of either subtracting one or two numbers.

    

            
inp = Solution()
n = [3,6,5,1,8]

print(inp.maxSumDivThree(n))