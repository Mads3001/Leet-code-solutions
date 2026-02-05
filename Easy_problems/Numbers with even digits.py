

# the receives a list of numbers. The code needs to return how many of the numbers have even digits.

def findNumbers(self, nums: list[int]) -> int:

    even_number_count = 0
    for number in nums:
        if not len(str(number)) % 2:
            even_number_count += 1

    return even_number_count

numbers = [12,345,2,6,7896, 288967, 29, 10, 111]



# a better method can be used by checking the bits


def findNumbers(self, nums: list[int]) -> int:

    even_number_count = 0
    for number in nums:
        if len(str(number)) & 1 == 0: # this checks if the first bit is zero. In all even numbers the first bit is zero, since the first bit represents 1.
            # that is much faster than doing modulo
            even_number_count += 1

    return even_number_count

print(findNumbers(0, numbers))