
# the code gets a string as a list with one letter as each element. The order of the list should be reversed.

def reverseString(self, s: list[str]) -> None:

    # it should be floor, since the middle element stays the same.
    for i in range(len(s) // 2):
        s[i], s[-(i + 1)] = s[-(i + 1)], s[i]

# this should do the same as .reverse()
# maybe this can actually be a oneliner?
# okay, the oneliner uses some other syntax that i don't really want to mess with.
# the fast approach would just be s = s[::-1] to reverse it. It is just reassigning instead of being worked inplace.


def reverseString(self, s: list[str]) -> None:

    s [:]= s[::-1] # this is the "pythonic solution" with slicing
    # this is actually pretty slow. that might be due to the other solution using two pointers, thus increasing the speed by 2.



def reverseString(self, s: list[str]) -> None:
    s.reverse() # the builtin reverse is maybe the fastest.
    # it is the fastest by far, because it is made in C with multiple optimizations not found with the python intepreter.

u = [1,2,3,4,5]
reverseString(0,u)
print(u)