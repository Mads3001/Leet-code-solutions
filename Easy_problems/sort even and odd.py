
# this also needs to be and in-place function.
# the input is a list of integers both even and uneven. It all the even integers should be sorted to the front.


class Solution:
    def sortArrayByParity(self, nums: list[int]) -> list[int]:
        
        num_of_even = 0
        for even_numbers in nums:
            if even_numbers & 1 == 0:
                num_of_even += 1
        times_switched = 0
        for i, number in enumerate(nums):
            if times_switched == num_of_even:
                break
            if number & 1 == 1: # if it is uneven

                for _ in range(i + 1, len(nums)): # it now searches for an even number it can switch with
                    if nums[_] & 1 == 0: # if it is even
                        nums[_], nums[i] = nums[i], nums[_]
                        times_switched += 1
                        break # it stops, when it has found the even number to switch with.
    # this should work, but is ineffecient due to it failing, when the only remaining elements are uneven.
    # we need to keep track of how many even numbers there are.
        return nums
    

def sortArrayByParity(self, nums: list[int]) -> list[int]:
        
    num_of_even = 0
    for even_numbers in nums:
        if even_numbers & 1 == 0:
            num_of_even += 1
    times_switched = 0
    for i, number in enumerate(nums):
        if times_switched == num_of_even:
            break
        if number & 1 == 1: # if it is uneven

            for _ in range(i + 1, len(nums)): # it now searches for an even number it can switch with
                if nums[_] & 1 == 0: # if it is even
                    nums[_], nums[i] = nums[i], nums[_]
                    times_switched += 1
                    break # it stops, when it has found the even number to switch with.
    # this should work, but is ineffecient due to it failing, when the only remaining elements are uneven.
    # we need to keep track of how many even numbers there are.
    return nums
numbers = [3,1,2,4,2, 45, 324, 324, 543, 678, 352, 563, 901]

print(sortArrayByParity(0, numbers))

# it works, but very slow.




# this is the better solution because it only iterates over the list once. The order of the sort is not important, so it works.
def sortArrayByParity(nums):
    left, right = 0, len(nums) - 1
    while left < right:
        if nums[left] % 2 > nums[right] % 2:
            nums[left], nums[right] = nums[right], nums[left]
        if nums[left] % 2 == 0:
            left += 1
        if nums[right] % 2 == 1:
            right -= 1
    return nums
