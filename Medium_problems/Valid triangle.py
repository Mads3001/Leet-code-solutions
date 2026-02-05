

# the code should tell how many valid triangles you can make with the array of numbers. Each number can only be used once on position.
# a triangle is valid, when the two small sides are bigger than the greatest side.

def triangleNumber(self, nums: list[int]) -> int:
    # we can simply make a loop that first selects the first side, then a loop that tries all other sides for the second side, and then at last all the third sides.
    # we can do it by first the first side and the second. Then the third side must be at least larger than the first two sides combined.
    count = 0

    # we need a way to not make duplicate triangles.
    # maybe a while loop is the better way to only parse once.

    # when the array is sorted, then we can just check the pair of each number under the greatest value
    nums.sort()
    # it is now sorted
    # we start in the end, so:
    n = len(nums)
    for i in range(n - 1, -1, -1): # we start at n-1 and walk towards -1 in increments of -1.
        left = 0 # starts with the smallest side length
        right = i - 1 # starts with the second smallest side length
        # then we check, if left + right is bigger than the side i.
        while left < right:
            if nums[left] + nums[right] > nums[i]: # nums[i] is the large side. it starts out by being small, but gets larger, when the for loop runs a couple times.
                count += right - left # all the values between left and right is valid, when it reaches this.
                right -= 1
            # if it isn't bigger, then we can either make i bigger (and thus the number smaller) and check again.
            else: # if the two sides aren't big enough, then it moves the left side to a bigger value. Just until left == right
                left += 1
    return count


        

# something is still wrong

input = [2,2,3,4]

print(triangleNumber(0,input))
