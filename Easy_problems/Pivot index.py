

# an array is given and the code need to find the pivot index. 
# A pivot index is when the sum of all indexes to the right of the index is the same as the sum of all the indexes to the left.
# we can start out by moving with two values.


def pivotIndex(self, nums: list[int]) -> int:
    # all the values to the right start out by being the sum of all.
    # the pivot index is not calculated into the values of left and right. It is neutral.

    lefties = 0
    righties = sum(nums)

    righties -= nums[0] # we need to remove the first index
    if lefties == righties: # if they start out by being equal, then the pivot index is zero.
        return 0
    

    for i in range(1, len(nums)):
        righties -= nums[i] # this subtracts. from righties, as it crawls over the array.
        lefties += nums[i - 1] # this adds to lefties, when it progresses over the array.

        if lefties == righties:
            return i # the index is returned, if there are a pivot index
    return -1 # if no such index exists, then it returns -1.

input = [1,7,3,6,5,6]
# input = [1,2,3]
# input = [2,1,-1]
print(pivotIndex(0, input))
