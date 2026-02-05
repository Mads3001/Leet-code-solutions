
# the input is an array of numbers.
# the array is split into two groups. The ones to the index i (including i) and those after.
# we should take the sum of those two groups and find whether the difference in sum is even. If they are, then that should be added to a count



from typing import List

class Solution:
    def countPartitions(self, nums: List[int]) -> int:
        left = sum(nums)
        right = 0
        count = 0
        for num in nums[:len(nums)]:
            right += num
            left -= num
            if abs(right - left) & 1 == 0:
                count += 1
        return count