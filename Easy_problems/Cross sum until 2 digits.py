
# the input is a string of a number. The code should take the two first digits in the number and find the cross sum and replace the two numbers.
# that should be repeated until the string only consists of 2 numbers.
# the code should then either return true or false, with the deciding factor being if the two remaining digits are equal or not.

# I read the question wrong. It isn't just the first two digits where you need the cross sum. This is a problem more like the pascals triangle, but reversed.


# I can write a function that should sum all the digits adding to the left digit, since the last digit is always unchanged.
# I can also write a recursive solution, which I'll try after.


class Solution:
    def hasSameDigits(self, s: str) -> bool: # you should instead maybe split s into an array.
        
        ls = list(s)
        l = len(s)

        while l > 2: # this stops, when the length has reached 2.
            for i, num in enumerate(ls[1:]):
                ls[i] = int(ls[i]) + int(num) # this also makes everything into integers.
            ls.pop() # this removes the last element for each iteration.
            l -= 1
        return ls[0] % 10 == ls[1] % 10


# this was one of the faster solutions. Not the fastest, but fast.

      


# now time for the recursive solution
class Solution:
    def hasSameDigits(self, s: str) -> bool:

        if len(s) == 2:
            return int(s[0]) % 10 == int(s[1]) % 10
        
        ls = list(s)

        for i, num in enumerate(ls[1:]):
            ls[i] = str(int(ls[i]) + int(num)) # this also makes everything into integers and then to strings, so it can be joined back together
        ls = "".join(ls)
        return self.hasSameDigits(ls[:-1])


inp = Solution()
print(inp.hasSameDigits("000000101"))


        