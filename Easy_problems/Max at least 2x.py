
# the code should determine, if the largest element is at least twice the size of the second element.

def dominantIndex(self, nums: list[int]) -> int:
    # it could be sorted, but I don't think it is the fastest.
    # finding the max two times or only iterating over the array once seem to be the smartest.

    max_in_list = max(nums)
    half = max_in_list/2
    for i in range(len(nums)):
        if nums[i] > half:
            if nums[i] != max_in_list:
                return -1
            if nums[i] == max_in_list:
                index = i
    return index


input = [3,6,1,0]
# input = [1,2,3,4]
print(dominantIndex(0, input))


# we can maybe also do it by storing two values of max. We have the current max and old max. That way we iterate over the list only once.
