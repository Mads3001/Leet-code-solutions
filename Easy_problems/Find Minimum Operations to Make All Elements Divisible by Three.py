
# the input is an array of numbers.
# we need to make them all divisible by 3.

# we can just take modulo three of them all. After that we can easily decide how much they need to be divisible.

from typing import List
class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        count = 0

        for num in nums:
            if num % 3:
                count += 1
        return count

# maybe i can do this as a oneliner




class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        return list(map(lambda num: min(3 - (num % 3), (num % 3) - 0), nums))