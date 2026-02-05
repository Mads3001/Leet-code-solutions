

# the input is an array of numbers, an integer k, and an integer that decides how many operations we can use per proposed solution.
# We can either add or subtract in the range of k to an element. We then need to find the maximum frequency of an element possible with the given values.


class Solution: # I'm nowhere near good enough to find a solution on my own, so I will copy one from the internet and follow the logic.
    def maxFrequency(self, nums: list[int], k: int, numOperations: int) -> int:
        # One of the approaches that can search for the max frequency uses the sliding window algorithm and the main solution also deals with ranges, so sorting is needed.
        nums.sort()
        # it is always easiest to have the current target (greedy solution) as an integer in the array.
        n = len(nums) # this is for the first iteration purposes.
        left = 0 # left and right is for the sliding window.
        right = 0
        i = 0 # also iteration purposes
        max_freq = 0 # since two algorithms will try to find the maximum we need to compare and store the maximum.

        while i < n: # this loop is the greedy loop that tries to find the max frequency for every pre-existing value in the array.
            target = nums[i]
            count = 0 # the current elements with the current target
            
            while i < n and nums[i] == target: # this takes all the elements that currently share the target value.
                count += 1
                i += 1
            
            # a new loop to try and include more elements to the right and left is then added.
            while left < n and nums[left] < target - k:
                left += 1
            while right < n and nums[right] <= target + k:
                right += 1
            
            max_freq = max(max_freq, min(right - left, count + numOperations)) # the maximum amount of elements with the same value is the values starting at target + the number of operations.
            # the right - left can be bigger, but we do not have enough operations to turn all of them into the target

            # if all the operations have been exhausted with this greedy algorithm, then we know, that there aren't any higher frequencies.
        if max_freq >= numOperations:
            return max_freq
            
        # the second algorithm searches widely without having a specific target in mind.
        left = 0
        max_freq_no_target = 0
        # the left is reset again.
        for right, val in enumerate(nums): # this just takes the first element and looks at the earlier elements to see, if they are in the range.
            while nums[left] < val - 2 * k:
                left += 1
            # the range is -2k, because the first following elements can also be increased by up to 1k. It only looks at earlier values and readjusts, so the final
            # target might be something near the middle.
            max_freq_no_target = max(max_freq_no_target, right - left + 1) # this just updates the one with the most possible values. It is still restricted by
            # the number of operations, but that will be checked for in the return statement.

        return max(max_freq, min(max_freq_no_target, numOperations)) # here the min is set, so the second algorithm can't go over the amount of operations.

