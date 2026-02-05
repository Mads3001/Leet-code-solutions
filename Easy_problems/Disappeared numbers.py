

# you get an array of n length with n integers. The intergers should be in range(1, n)



def findDisappearedNumbers(self, nums: list[int]) -> list[int]:
    # we can start out by sorting the input.
    
    full_set = set([i for i in range(1, len(nums) + 1)])
    nums.sort()
    nums_set = set(nums)

    full_set = full_set.difference(nums_set)

    return list(full_set)
    

input = [34,47352,47293,25351,41449,19033,22862,43976,29561,49286,12083,18596,17524,959,38206,10129,29953,10639,30597,43486,39440,24856,46705,29640,12251,17596,29222,11442,48631,7269,47357,29364,234,1]

print(findDisappearedNumbers(0, input))



def findDisappearedNumbers(self, nums: list[int]) -> list[int]:
    # we can make it a set instead
    num = set(nums)
    res = []
    for i in range(1,len(nums)+1):
        if i not in num:
            res.append(i)
    return res

# i originally tried by using a list, but it is nescessary to convert to a set, because searching in a list is slow. 
# i also did it in the same list by removing and appending stuff. That made the implementation too slow.
# this solution is technically O(n)