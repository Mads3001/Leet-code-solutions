
# an array and a target is given. the code needs to find out the minimum length of elements in the array that could be greater or equal to the target.
# Since it is a subarray, then it must be a continious portion of the array. We can't sort it then.


# instead we'll implement the a window slide algorithm that slides over the array.
def minSubArrayLen(self, target: int, nums: list[int]) -> int:
    if sum(nums) < target: # if the target can't be reached
        return 0
    res = 0
    i = 0
    ie = 0
    length = float('+inf')
    while i < len(nums):
        if res < target:
            res += nums[i]
            i += 1
        while res >= target: # this should instead be a while loop, since one large value can call for removing multiple small ones.
            length = min(length, i - ie)
            res -= nums[ie]
            ie += 1
    return length

#if length > i - ie:
#   length = i - ie
# this is a slow implementation.
# length = min(length, i - ie) is faster
t = 11
n = [1,2,3,4,5]

print(minSubArrayLen(0,t,n))


# making the first while loop into a for loop could also improve speed.
def minSubArrayLen(self, target: int, nums: list[int]) -> int:
    if sum(nums) < target: # if the target can't be reached
        return 0
    res = 0
    ie = 0
    length = float('+inf')
    for i, number in enumerate(nums):
        if res < target:
            res += number
        while res >= target: # this should instead be a while loop, since one large value can call for removing multiple small ones.
            length = min(length, i - ie + 1)
            res -= nums[ie]
            ie += 1
    return length

# the for loop doesn't really improve anything.