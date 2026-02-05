
# the input is two lists of potions and spells and an integer called success.
# the power of a combination is the power of the spell times the power of the potion.


def successfulPairs(self, spells: list[int], potions: list[int], success: int) -> list[int]:
    # we need to return the amount of combinations that have at least "success" as the strength
    # the output should be a list of how many successes the a certain spell has.

    # the lists can be very long, so it can make sense to try and sort the potions in ascending order. After the first succesful value the rest should also be successful.
    combinations = []
    potions.sort()
    for spell in spells:
        minimum_potion = success / spell # we can compare all the potions to minimum potion.

        left, right = 0, len(potions) - 1 # we start by writing down the index of the left and right.
        idx = len(potions)  # default index if no potion is valid and the while loop can't find and reassign idx.

        while left <= right: # this is the loop that decides which half to search and give new left and right bounds.
            mid = (left + right) // 2
            if potions[mid] >= minimum_potion: # if the middle is is greater, then a new left side is marked and ready to be searched.
                idx = mid  # update index to mid
                right = mid - 1  # search on the left half to find earlier valid potion
            else:
                left = mid + 1  # search on the right half
                # if the left side is too small, then the right side is searched.

        # count how many potions from idx to end (if idx not changed, means 0 successes)
        combinations.append(len(potions) - idx)
                
    return combinations

# the solution works, but there are too many potions, so we need binary search to find the point of the potions being strong enough.
# binary search have been implemented.

input_spells = [5,1,3]
input_potions = [1,2,3,4,5]
input_success = 7
print(successfulPairs(0,input_spells,input_potions,input_success))

