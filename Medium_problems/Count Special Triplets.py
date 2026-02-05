
# the input is an array of numbers.

# a triplet is three numbers where the leftmost and rightmost number is twice the value of the middle number


# we need a fast way to count the occurrence of numbers.

# we just need to count the unique possibilities with a certain number as the middle with a varying amount of valid sides.
# with a given middle the amount of possible permutations are right * left, where those are the amount of valid numbers to the right and to the left.
# we can do that with an array for each value in the original array

from typing import List
class Solution:
    def specialTriplets(self, nums: List[int]) -> int:
        count = 0
        freq_map = {}
        numbers = set(nums)
        l = len(nums)
        for num in numbers:
            freq_map[num] = [[], -1]
        # now a frequency map is made for all unique values.
        # we now make the frequency map by appending tuples with (index, amount_seen)
        for i, num in enumerate(nums):
            freq_map[num][1] += 1
            freq_map[num][0].append((i, freq_map[num][1]))
        # now the frequency map is created.
        # I can now create a binary search to find the closest i stored.
            
        for i, num in enumerate(nums):
            if num * 2 in numbers:
                le = len(freq_map[num * 2][0])
                right = le - 1
                left = 0
                idx = -1
                while left <= right:
                    middle = (left + right) // 2
                    if freq_map[num * 2][0][middle][0] <= i:
                        idx = middle
                        left = middle + 1
                    else:
                        right = middle - 1
                # the smallest idx larger or equal to i is found and the value can now be found.
                if idx >= 0:
                    count +=  freq_map[num * 2][0][idx][1] * (freq_map[num * 2][1] - freq_map[num * 2][0][idx][1])
        return count         




inp = Solution()
n = [0,1,0,0]
n = [8,4,2,8,4]
print(inp.specialTriplets(n))





