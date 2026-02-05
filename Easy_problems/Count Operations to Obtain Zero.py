
# the input is two numbers. The smallest number is subtracted from the largest number and the largest number is reassigned.
# That happens until 1 of the numbers are 0.
"""
class Solution:
    def countOperations(self, num1: int, num2: int) -> int:
        count = 0
        while num1 != 0 and num2 != 0:
            if num1 >= num2:
                num1 -= num2
                count += 1
            else:
                num2 -= num1
                count += 1
            
        
        return count

n1 = 2
n2 = 3

inp = Solution()

print(inp.countOperations(n1, n2))
"""
# I can also write a recursive solution.


def countOperations(num1: int, num2: int, steps=0) -> int:
        
    count = steps
    if num1 == 0 or num2 == 0:
        return count


    if num1 >= num2:
        num1 -= num2
        count += 1
    else:
        num2 -= num1
        count += 1
    
    return countOperations(num1,num2, steps=count)

print(countOperations(2,3))



# the best solution is:
class Solution:
    def countOperations(self, num1: int, num2: int) -> int:
        a, b = num1, num2
        ops = 0
        while a > 0 and b > 0:
            if a < b:
                a, b = b, a
            ops += a // b
            a %= b
        return ops