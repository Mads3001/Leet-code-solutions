
# the description for this problem is really bad.
# the input is an array and two integers. The output should be two subarrays.

# some of the output should be the x-sum. The x-sum is the sum of the x highest frequencies of elements in the array.
# If an array has a bunch of 2s and 4s and x = 2, then it should return the sum of all the 2s and 4s.
# If the array also has 1s and x = 3, then it needs to include another element in the x-sum. Thus it is the sum of all the 1s, 2s and 4s.
# the x-sum needs to be run on a subarray. The length of the subarray it needs to be run on is signified by the input k.

# the array that gets returned needs to have "n - k + 1" elements. That is due to how many unique subarrays with length k can fit in the original array.


from typing import List
class Solution:
    def findXSum(self, nums: List[int], k: int, x: int) -> List[int]:

        ans = [] # the answer array at the end.

        # we need a function that can find the x-sum of a subarray. This clears up the redundant code.
        def XSum(arr: List[int], l: int) -> int:
            if len(arr) <= l:
                return sum(arr)
            unique = list(set(arr))
            if len(unique) <= l: # another safeguard, if there aren't enough unique elements.
                return sum(arr)
            for i, value in enumerate(unique):
                unique[i] = (arr.count(value), value) # the first is the frequency and the second is the value.
            unique.sort(reverse=True) # it will sort by the frequency. If tied, then the highest value will be prioritized.
            count = 0
            for _ in range(l):
                count += unique[_][0] * unique[_][1] # this becomes slow, if the count is very high or the x is very high.
            return count
        
        # now we need to feed the subarrays.
        for _ in range(len(nums) - k + 1): # this is the amount of elements in the return array.
            ans.append(XSum(nums[_:k + _], x))
        
        return ans


inp = Solution()

#n = [1,1,2,2,3,4,2,3]
#k = 6
#x = 2
n = [1,4,4,4]
k = 3
x = 2
print(inp.findXSum(n,k,x))


# clean without much commentary


class Solution:
    def findXSum(self, nums: List[int], k: int, x: int) -> List[int]:

        ans = [] 

        def XSum(arr: List[int], l: int) -> int: # function each subarray needs to go through
            count = 0 # X-sum of an array

            if len(arr) <= l: # edge case with length needed exceeding actual length
                return sum(arr)
            
            unique = list(set(arr))

            if len(unique) <= l: # edge case with length needed exceeding unique elements
                return sum(arr)
            
            for i, value in enumerate(unique):
                unique[i] = (arr.count(value), value) # (frequency, value)
            
            unique.sort(reverse=True) # sort by frequency first. value if tied. (trick with tuples)
            
            for _ in range(l):
                count += unique[_][0] * unique[_][1] # frequency * value
            return count
        
        for _ in range(len(nums) - k + 1): # the answer need to be of length "n - k + 1", since that amount of subarrays exist.
            ans.append(XSum(nums[_:k + _], x)) # every subarray is fed to the Xsum function
        
        return ans


