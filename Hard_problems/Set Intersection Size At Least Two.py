
# The input is an array with intervals. The intervals are [start, end] where the numbers are inclusive.
# The output should be the length of the shortest array, that contains at least two numbers from each interval. These are the intersections of the interval.
# We could visualize the problem by laying out railroad tracks adjacent to each other. We then take the numbers with most intersections, where we make sure to have --
# -- two numbers from each interval.

# I have an idea for a naive approach that might work.
# we start out by putting the frequency of each number in the intervals into a hashmap.
# then we start going through each interval and picks the number with the highest frequency, if there aren't numbers from that interval in the result set, then --
# the number with the highest frequency is added to the set from the interval we're looking at.


# we could also make this into the question of taking the smallest or biggest number in the interval. We could start out by sorting the intervals.
# When we start out with the smallest interval, then we know every single interval after that one has a bigger number.
# We can then start out by taking the largest two integers from the first interval.
# When we go to the next interval, then we can check if those two numbers also are in present in the next. If one of or both of them aren't, then we take the biggest from --
# that set because everything after that is bigger. We then add either one or two new values, when they aren't in the seen.

from operator import itemgetter
from typing import List
class Solution:
    def intersectionSizeTwo(self, intervals: List[List[int]]) -> int:

        intervals = sorted(intervals, key=itemgetter(1)) # sorts by the second element instead of the first.
        l = 0 # length of the hypothetical set with at least two numbers from each interval.
        last_added = [-1] * 2 # the two numbers present in the last interval. The interval can start at 0, so -1.

        for interval in intervals:
            if last_added[0] < interval[0] and last_added[1] != interval[1]: # this will replace the lowest value, if needed.
                l += 1
                last_added[0] = interval[1]
                last_added.reverse() # the new value is now the greatest, so we switch the order
                
            if last_added[0] < interval[0]: # this will replace the previous highest value if needed. (The new lowest value).
                # if that value is also too low, then we replace it with the new greatest minus 1.
                l += 1
                last_added[0] = interval[1] - 1
        return l
    

# storing the newly added items might be a better way.
            
i = [[1,3],[3,7],[5,7],[7,8]]
# i = [[2, 3], [3, 4], [3, 6], [2, 7], [6, 8], [1, 9], [8, 15], [56, 78], [19, 100]] after sorting
# 1. [2,3] l=2, [3,4]
inp = Solution()
print(inp.intersectionSizeTwo(i))
                
                
            
            





