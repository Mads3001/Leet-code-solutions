

# the code is very much like twosum, where the function gets N and needs to return two numbers that added equates to N. The catch is, that there cannot be a zero in it.

def getNoZeroIntegers(self, n: int) -> list[int]:
    return_list = []

    diff = 0

    # half = n // 2 # it is just faster to take the full number and iterating from there in most cases.

    while "0" in str((diff)) or "0" in str((n - diff)):
        diff += 1
    return_list.append(diff)
    return_list.append(n - diff)
    return return_list

    


number = 1000

print(getNoZeroIntegers(0, number))

