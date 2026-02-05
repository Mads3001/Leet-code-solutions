
# this code should assess, if a string of parentheses are valid.
# they should be evaluated by a stack.
"""
    Open brackets must be closed by the same type of brackets.
    Open brackets must be closed in the correct order.
    Every close bracket has a corresponding open bracket of the same type.
"""

# we just need to check how many are open and how many are closed at the current moment.
# the "*" is a wild card that can be any.
# okay, I read the problem wrong
# This is a solution for the original problem
class Solution:
    def isValid(self, s: str) -> bool:
        # we should make a stack of the next expected bracket
        stack = []
        brackets = {}
        brackets["("] = ")"
        brackets["["] = "]"
        brackets["{"] = "}"
        for c in s:
            if c in brackets:
                stack.append(brackets[c]) # appends the next expected
            elif stack:
                if c == stack[-1]:
                    stack.pop()
                else:
                    return False
            else:
                return False
        if stack:
            return False
        return True






        
# I could make it more readable, by having a list of things to check for, but this could work.
# it works, but not for wild cards. If the wild cards are needed to close something, then my code breaks.

inp = Solution()
s = "()"
print(inp.isValid(s))

# i was close to a valid solution.
# I was just trying to solve the wrong problem.


# this is another problem i tried to solve.

    
class Solution:
    def checkValidString(self, s: str) -> bool:
        leftMin, leftMax = 0, 0

        for c in s:
            if c == "(":
                leftMin, leftMax = leftMin + 1, leftMax + 1
            elif c == ")":
                leftMin, leftMax = leftMin - 1, leftMax - 1
            else:
                leftMin, leftMax = leftMin - 1, leftMax + 1
            if leftMax < 0:
                return False
            if leftMin < 0:
                leftMin = 0
        return leftMin == 0
        
                
            
