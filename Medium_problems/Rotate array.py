
# we need to rotate the array in a cyclical manner. That means if it needs to be shifted by 3, then all the last 3 elements will become the 3 first elements.
# we can just take the and edit the original array shifted by k.

class Solution:
    def rotate(self, nums: list[int], k: int) -> None:
        k = k % len(nums)
        nums[:] = nums[len(nums) - k:] + nums[:len(nums) - k]


inp = Solution()
l = [1,2,3,4,5,6,7]
inp.rotate(l, 3)

print(l)
