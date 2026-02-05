
# the input is an array of numbers, which each number is supossed to be unique. there are two duplicates though. The duplicates needs to be found.
# the output should be the two duplicates from the array.
# the numbers are from 0 to n-1 where n is the length of the array.
# we can sort and compare the index of the number to the number

from typing import List
class Solution:
    def getSneakyNumbers(self, nums: List[int]) -> List[int]:

        nums.sort()
        sneaky = []
        for i, number in enumerate(nums):
            if nums[i - 1] == number:
                sneaky.append(number)

        return sneaky




# this makes the space complexity O(1), but time complexity O(N log(N)) due to sorting.
# using a set makes the time complexity lower, but increases space complexity.


class Solution:
    def getSneakyNumbers(self, nums: List[int]) -> List[int]:

        seen = set()
        sneaky = []
        for number in nums:
            if number not in seen:
                seen.add(number)
            else:
                sneaky.append(number)
        return sneaky
    
n = [7,1,5,4,3,4,6,0,9,5,8,2]

inp = Solution()

print(inp.getSneakyNumbers(n))