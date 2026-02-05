
# this function takes a list.
# the function should then check, if there's elements that are double another element.

def checkIfExist(self, arr: list[int]) -> bool:
    
        
    found_values = []

    for number in arr:

        found_values.append(number)
        if (number * 2) and (number * 2) != number in found_values: # since there can be duplicates of the same value a dictionary may be useful.
            return True
        if (number / 2) and (number * 2) != number in found_values:
            return True
    return False


array = [-20,8,-6,-14,-19,14,0,0]
print(checkIfExist(0, array))

def checkIfExist(self, arr: list[int]) -> bool:
    dictionary = {}
    dictionary[0] = 0
    for number in arr:
        dictionary[number] =  1 + dictionary.get(number, 0)


    if dictionary[0] > 1: # if there's two values of zero in the dictionary, then it will return true.
        return True

    for number in dictionary:

        if number * 2 in dictionary and number!= 0:
            return True
    return False

print(checkIfExist(0, array))


# this solution works and is memory effecient. 0 was a bad edge case of that code.

# a better solution from the internet did as the problem stated and just kept track of index instead

def checkIfExist(self, arr: list[int]) -> bool:
    dic = dict(int)
    for i,n in enumerate(arr):
        dic[n] = i

    for i in range(len(arr)):
        double = 2 * arr[i]
        if double in dic and dic[double] != i:
            return True
    return False 

# this circumvents the problem with 0 in my code.