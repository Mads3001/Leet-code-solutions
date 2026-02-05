
# the input is a number. It can be created by an amount of perfect squares (natural number x^2)
# the output should be the amount of perfect squares.

# we can start by precomputing squares until a square reaches n.

from collections import deque

class Solution:
    def numSquares(self, n: int) -> int:

        squares = [1]

        root = 2
        while squares[-1] < n:
            squares.append(root**2)
            root += 1
        
        if n in squares:
            return 1
        
        queue = deque()
        queue.append(0)
        visited = {}
        visited[0] = 0

        # now for the bfs loop
        while n not in visited:
            for square in squares:
                num = queue[0]
                num += square
                if num not in visited:
                    visited[num] = 1 + visited[queue[0]] # the amount of steps to reach it.
                    queue.append(num)
            queue.popleft()
        return visited[n]



# a dynamic approach would be as following:

import math

class Solution:
    def numSquares(self, n: int) -> int:
        dp=[0]*(n+1) # it creates an array with n + 1 cells.
        for i in range(1,n+1):
            dp[i]=i
            for j in range(1,int(math.sqrt(i))+1):
                dp[i]=min(dp[i],dp[i-j*j]+1)
        return dp[n]
    

"""
    dp is created to store the least number of perfect squares needed for each number from 0 to n.
    The list dp is initialized with zeros, where dp[i] will eventually hold the solution for the number i.
    A loop iterates over each number from 1 to n (inclusive). For each number i, it tries to find the least number of perfect squares needed to sum up to i.
    Inside the loop, dp[i] is initialized with the maximum possible value i, assuming that the worst case would be summing i 1's (each 1 is a perfect square).
    Another loop iterates over each perfect square less than or equal to i, represented by the variable j. It iterates from 1 to the square root of i, because any perfect square larger than the square root of i would exceed i.
    Inside the inner loop, dp[i] is updated by considering the possibility of summing up to i using the current perfect square jj, along with the previously computed solution for i - jj. So, dp[i] is updated to the minimum of its current value (dp[i]) and dp[i - jj] + 1, where +1 represents the current perfect square jj.
    After the outer loop completes, dp[n] holds the least number of perfect squares needed to sum up to n, which is then returned as the result.
"""

"""
For n = 12, the function computes dp[12] which represents the least number of perfect squares needed to sum to 12. 
It calculates the minimum of dp[12], dp[12-1*1] + 1, dp[12-2*2] + 1, and dp[12-3*3] + 1, which are dp[12], dp[11] + 1, dp[8] + 1, and dp[3] + 1 respectively. 
The result is 3 because dp[3] + 1 has the minimum value among them. Therefore, the output is 3.
"""        
# this is a result of how the perfect squares work.s

        

        
