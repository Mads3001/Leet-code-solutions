

# the incoming array needs to be assessed. if it's a mountain array. It needs to always be increasing and then always be decreasing after the top. 
# It cannot have points where it is not increasing.

# It also needs to increase at least once, so it has a peak.

def validMountainArray(self, arr: list[int]) -> bool:
    # we can start by monitoring, if it is increasing or decreasing

    if len(arr) < 3: # if there's fewer than 3 elements in the array, then it can't be a mountain.
        return False
    if arr[0] == max(arr): # the peak cannot be the first or last element
        return False
    if arr[-1] == max(arr):
        return False


    decreasing = False
    has_increased = False
    i = 0
    while i < len(arr) - 1: # len(arr) goes up to index + 1. Therefore to stay within index it should be -1
        if arr[i] == arr[i + 1]: # if the mountain is flat at this point it is false.
            return False
        if not decreasing: # if it is not decreasing, then every element should be larger.
            if arr[i] < arr[i + 1]: # the second element should be larger.
                i += 1
            else: # if it is not increasing, then it is now decreasing.
                decreasing = True
        if decreasing:
            if arr[i] > arr[i + 1]: # then the first element should always be larger than the next.
                i += 1
            else:
                return False
    # if it is strictly increasing, then followed by strictly decreasing, the it is a mountain.
    # we need to check, if it has decreased.
    return True

mount = [0,1,2,1,0]

print(validMountainArray(0, mount))

# this final version works, but is not the fastest, nor the least memory intensive.
# apperently it beat 55 percent in time the first submission. (26,44 in memory)
# the second submission it beat 81,96 percent in memory utilization. (23,11 in time)
# that is without changing anything.