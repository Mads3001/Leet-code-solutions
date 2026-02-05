
# the code receives an array of numbers. All the zero values should be moved to the end. The rest of the elements should retain the same order.


def moveZeroes(self, nums: list[int]) -> None:
    # this can be done by making a for loop and checking if a value is zero. It should then pop the zero and append it instead.
    # It could also keep track of the position of the zero and then switch places with the element to the right.
    # it didn't work since it got stuck. maybe keeping track of the zeroes are a good thing.

    i = 0 # the current index that are worked on.
    i_stop = len(nums) # this is where the the 
    while i < i_stop: # the loop gets stuck, when it reaches the end where the zeroes are without keeping track of where to stop.
        if nums[i] == 0: # if the element is zero, then it is added to the end of the array.
            nums.pop(i) # this makes the element to the right take the index instead.
            nums.append(0)
            # to make it not loop forever we need to keep in mind what index it needs to stop at.
            i_stop -= 1
        else: # if the element is not zero, then i is increased by one until i finds another value of zero.
            i += 1
# that solution works due to keeping track of where the original end of array has been moved to.
      



# the solution like bubblesort.
# the function should keep track of the first element that is zero
""""
def moveZeroes(self, nums: list[int]) -> None:
    i = 0 # this marks the location of the current analyzed index.
    s = 0 # this is the index the function should search after.
    while i < len(nums):
        if nums[i] == 0:
            s = i + 1 # this marks the zero. It can't handle multiple zeroes in a row though.
        # instead the algorithm should search for a non-zero value after it finds a zero.
        while nums[i] == 0:
            if nums[s] != 0:
                nums[i] = nums[s]
                nums[s] = 0
                i += 1
            else:
                s += 1
"""
# the code didn't work, since it can't take into account if there are many more non-zero values after the zeroes. 


numbers = [0,0,0,0,1]
moveZeroes(0,numbers)
print(numbers)


# the better solution from the internet is:

class Solution:
    def moveZeroes(self, nums: list[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        j = -1

        for i in range(n):
            if nums[i] == 0:
                j = i
                break # this stops the for loop once it has reached a condition. (once it has reached the first zero)

        if j == -1:
           return  # the function stops, if there are no zeroes.      

        m = j + 1 # it now searches for the first non-zero value after the first zero. 
        for i in range(m,n): #
            if nums[i] != 0:
                nums[i], nums[j] = nums[j], nums[i] # this makes the zero switch places with the first non-zero value. 
                j += 1   # it increases j by one and makes the zero move up the indexes and switch places with non-zero values. This works until the last non-zero value have been found.