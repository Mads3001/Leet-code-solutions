
# the input is a delimited string, where there is a number and a string in square brackets. The number denotes how many times the string should be repeated.
# there can be nested strings:
# e.g. s = "3[a2[c]]", then the output should be "accaccacc"

# we need a system to parse the information. We should process each bite of a sequence.
# e.g. we should break "3[a2[c]]4[t]3[ri]" into the composites 3[a2[c]] 4[t] 3[ri]
# we could also take the naive approach where we parse over the string multiple times.
# we could loop over the string with a sliding window approach and create a stack for unraveling a composite bite.

# python also has natural layering system and multiplication for strings.
# we could also just use that by creating an expression to evaluate.
# that would work, since the integers are at least 1, so a multiplication by 1 should be simple.
class Solution:
    def decodeString(self, s: str) -> str:
        if not s: return ""

        

        # we should have some kinds of actions to for the stack
        self.i = 0
        return self.decode(s)
        # instead of using some weird nesting to unravel, we could also just use some recursion
    def decode(self, s: str) -> str:
        l = len(s)
        num = 0
        res = ""
        while self.i < l:
                
            c = s[self.i]
            if c.isdigit(): # this harvests the number before
                num = num * 10 + int(c)
                self.i += 1
            elif c == "[": # if it is nested, then it starts a recursive call
                self.i += 1    
                inner = self.decode(s) # the recursive call also applies the number multiplication
                res += inner * num
                num = 0
            elif c == "]": # if it just closes, then it returns
                self.i += 1
                return res
            else:
                res += c # if neither is true, then it just adds the character
                self.i += 1

                


        # we should start out with the sliding window algorithm.




