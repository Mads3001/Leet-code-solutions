

# this function takes the input of a list of integers and then an integer.
# the function should return the list of indexes of the two numbers added, 
# which would reach the target.
def twoSum(self, nums: list[int], target: int) -> list[int]:
    indexes = []
    for index1, value1 in enumerate(nums): 
        remain = target - value1
    # this takes the first systematically goes over the values.
    # it notes the remain, which is the other value needed.
        for index2, value2 in enumerate(nums): 
            # this goes over the other number and keeps the index 
            if value2 == remain and index1 != index2:
                indexes.append(index1)
                indexes.append(index2)
                return indexes
    return "no two sum found for {target} in this list"

# This solution is slow, so you can instead make a faster solution by using a hash map.



def twoSum(self, nums: list[int], target: int) -> list[int]:
    hash_num = {} # dictionary to store, if a value has been seen
    indexes = []

    for index1, value1 in enumerate(nums): 
        # this fills the dictionary, where each key (value) is assigned their index as value.
        # that way we can check if the keypair for a value exists.
        hash_num[value1] = index1

    for index2, value2 in enumerate(nums):
        remain = target - value2
        if remain in hash_num and index2 != hash_num[remain]:
            indexes.append(hash_num[remain])
            indexes.append(index2)
            return indexes
    return "no two sum found for {target} in this list"
