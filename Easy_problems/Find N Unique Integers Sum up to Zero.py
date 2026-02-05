

# The input to the function is an integer N. 
# the output needs to consist of a list with N integers that all adds up to zero. They all need to be unique.

def sumZero(self, n: int) -> list[int]:
    i = -n
    numbers = []
    num = 0
    while (num + 1) < n: # this fills the list with a bunch of negative numbers. 
        numbers.append(i)
        i += 1
        num += 1
    rest = n - sum(numbers)
    numbers.append(rest)
    return numbers


