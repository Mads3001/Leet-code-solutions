
# this time you need to merge to arrays and then return the final array sorted.
# an easy method is just extending array two unto array one and then sorting.


def merge(self, nums1: list[int], m: int, nums2: list[int], n: int) -> None:
    """
    Do not return anything, modify nums1 in-place instead.
    """
    while len(nums1) > m: # this removes the extra zeroes in the nums1 list. They are not helping, when using python.
        nums1.pop()
    nums1.extend(nums2) # extend instead takes and instead a list by another list
    nums1.sort()




nums1 = [1,2,3,0,0,0]

nums2 = [2,5,6]


merge(0, nums1, 3, nums2, 3)

print(nums1)


# a better version could be:

def merge(self, nums1: list[int], m: int, nums2: list[int], n: int) -> None:
    for i in range(m, m + n):
        nums1[i] = nums2[i - m]
    nums1.sort()
# that is because it instead just overwrites the empty values in num1 from num2. It decides where to start based on m and until m + n, due to it needing to loop n times.