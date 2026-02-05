
# the input is a large array of elements. The code must find subarrays that are strictly increasing in value as the index rises.
# the returned value should be the maximum length of the subarrays (they should be adjacent to each other) k.
# we should be able to solve the problem with a sliding window approach. The sliding window should just mark the largest amount of increasing elements in a line.
# the length of the subarrays is then just found with a floor division of 2.
# the code just notes the maximum length while it pans over the array.



# i was wrong in my approach. It should be different.
# when the code finds a decrease it should look the length of the first subarray and then look for a corresponding one just after i.



def maxIncreasingSubarrays(self, nums: list[int]) -> int:

    longest = 1 # the default value is 1 in this problem.

    i_r = 0 # the left and right parts of the window
    i_l = 0
    lengths = []
    while i_r < len(nums) - 1: # this should check through the whole array
        if  nums[i_r] < nums[i_r + 1]: # the index should always be positive.
            i_r += 1 # the next value is valid and the first part of the window slides over and increases the length.
        else: # if the next element isn't greater, then i and ie should be measured and it starts to try and find a new part of the increasing array.
            
            lengths.append(i_r - i_l + 1) # this adds the length of the current subarray to a list.

            if len(lengths) == 2: # if more than two elements, then the earliest element is removed.
                longest = max(longest, min(lengths)) # min(lengths) is the shortest length of the two subarrays.
                longest = max((i_r - i_l + 1) // 2, longest)
                lengths.pop(0) # I could use deque, but with so few elements it should still be fast enough.
            else:
                longest = max(lengths[0] // 2, longest)

            i_l = i_r + 1 # a new starting point is chosen.
            # the loop gets stuck, so i must also increase
            i_r += 1
            # now a while loop should look for the length of increasing elements again.
    # this also has the problem, if it ends by increasing the length.
    # I need to write a check that cathes, if the loop without possibly checking if the new length is the longest.

    if i_l != i_r: # if this hasn't happened, then it will check one last time before returning
        
        if lengths: # is only hit, if there's any elements in the list
            lengths.append(i_r - i_l + 1)
            longest = max(longest, min(lengths)) 

        longest = max((i_r - i_l + 1) // 2, longest)
    if len(lengths) == 1:
        longest = max(lengths[0] // 2, longest)
        
    return longest


# the longest subarray can also be one big subarray, so I also need to check if one subarray is large enough to be both subarrays.
# inp = [2,5,7,8,9,2,3,4,3,1]
# inp = [1,2,3,4,4,4,4,5,6,7]
# inp = [-15,-13,4,7]
# inp = [-8,0,5,18,-9]
inp = [-5,3,11,13,20,20,-14]
# maxIncreasingSubarrays(0,inp)

print(maxIncreasingSubarrays(0,inp))


# very cluttered, but working solution.


# clean version




def maxIncreasingSubarrays(self, nums: list[int]) -> int:

    longest = 1 # minimum return value (default)
    i_r = 0 # right and left sliding window index.
    i_l = 0
    lengths = []
    while i_r < len(nums) - 1: 
        if  nums[i_r] < nums[i_r + 1]: 
            i_r += 1 
        else: 
            lengths.append(i_r - i_l + 1) 
            if len(lengths) == 2:
                longest = max(longest, min(lengths)) 
                longest = max((i_r - i_l + 1) // 2, longest)
                lengths.pop(0) 
            else:
                longest = max(lengths[0] // 2, longest) # case with 1 large subarray and only 1 other (last) value.
            i_l = i_r + 1 
            i_r += 1
 

    if i_l != i_r: # if last action was adding to a subarray
        
        if lengths: # if there are multiple subarrays
            lengths.append(i_r - i_l + 1)
            longest = max(longest, min(lengths)) 

        longest = max((i_r - i_l + 1) // 2, longest) # case with only one subarray.
    if len(lengths) == 1: # case with 1 large subarray and only 1 other (first) value.
        longest = max(lengths[0] // 2, longest)
        
    return longest

# i am frankly going insane.