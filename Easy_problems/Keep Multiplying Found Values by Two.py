
# the input is an array and an integer "original"
# if original is found in the array, then, "original" should be multiplied by 2. That process loops until original is no longer in the array.

from typing import List
class Solution:
    def findFinalValue(self, nums: List[int], original: int) -> int:
        n = set(nums)
        while original in n:
            original *= 2
        
        return original