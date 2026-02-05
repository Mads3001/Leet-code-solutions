
# the input will be a list.
# each element in the list should look at the greatest value to the right of that element. The original element should then become the that value.

def replaceElements(self, arr: list[int]) -> list[int]:

    # since it is the largest integer to the right, then we can maybe loop backwards this time, by starting with subscribting.
    # keeping account of the largest value seen.
    largest_value = -1 # it should start with -1, since it will then make the rightmost element 1.
    tmp = 0
    for i in range(1, len(arr) + 1): # subscribting starts with -1.
        tmp = arr[-i]
        arr[-i] = largest_value
        if tmp > largest_value:
            largest_value = tmp

    # this might not work, if it doesn't edit the array properly.
    return arr

input = [1274, 2178, 4983, -123, 843, 534]

print(replaceElements(0, input))

# it worked and scored surprisingly well compared to other people's submissions.