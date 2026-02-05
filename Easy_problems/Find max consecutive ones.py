



# memory efficient one
def findMaxConsecutiveOnes(self, nums: list[int]) -> int:
    consecutive_nums = []
    consecutive_ones = 0
    for num in nums: 
                
        if num == 1:
            consecutive_ones += 1
        
        else:
            consecutive_nums.append(consecutive_ones)
            
            consecutive_ones = 0
    
    consecutive_nums.append(consecutive_ones)
    
    return max(consecutive_nums)



numbers = [1,1,0,1,1,1]
# print(max(numbers))
print(findMaxConsecutiveOnes(0, numbers))


# time efficient one
def findMaxConsecutiveOnes(self, nums: list[int]) -> int:
    max_consecutive_ones = 0
    consecutive_ones = 0
    for num in nums: 
                
        if num == 1:
            consecutive_ones += 1
        
        else:
            if consecutive_ones > max_consecutive_ones:
                max_consecutive_ones = consecutive_ones
            consecutive_ones = 0
    if consecutive_ones > max_consecutive_ones:
        max_consecutive_ones = consecutive_ones
    
    return max_consecutive_ones