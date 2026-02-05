
# the input is an array of 0s and 1s.
# We need to find out if a certain portion of the binary number is divisble by 5. The number grows by one element in the array at a time.
# e.g. [1,0,1]. The first: 1, second: 10, third: 101.
# the number grows by doubling and sometimes adding 1, if the new number is one.

from typing import List
class Solution:
    def prefixesDivBy5(self, nums: List[int]) -> List[bool]:
        ans = []
        count = 0
        for num in nums:
            count *= 2
            if num:
                count += 1
            ans.append(not bool(count % 5))
        return ans
        
# I will maybe write a bit manipulation version of this where you use << to multiply it by 2.
class Solution:
    def prefixesDivBy5(self, nums: List[int]) -> List[bool]:
        ans = []
        count = 0
        for num in nums:
            count = count << 1
            if num:
                count += 1
            ans.append(not bool(count % 5))
        return ans