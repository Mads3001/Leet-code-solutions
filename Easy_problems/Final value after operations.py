
# there is only 4 operations that can happen
# ++X and X++ increments x by 1.
# --X and X-- decrements x by 1.
# x starts out as 1

# we can just make a for loop and check for either a plus or minus symbol in the string.

def finalValueAfterOperations(self, operations: list[str]) -> int:

    x = 0

    for operation in operations:
        if "+" in operation: # this only makes one check, because it can only be one or the other.
            x += 1
        else:
            x -= 1

    return x


# maybe the "in" operation is slow. If the full strings are checked for it might be faster or use less memory.


def finalValueAfterOperations(self, operations: list[str]) -> int:

    x = 0

    for operation in operations:
        if operation == "++X" or operation == "X++": # this only makes one check, because it can only be one or the other.
            x += 1
        else:
            x -= 1

    return x

# it doesn't really make a diffrence. It is just the solution checker being sluggish again.