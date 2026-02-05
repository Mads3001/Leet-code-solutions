
# we start with an amount of full water bottles.
# we can drink those and turn them empty. 
# we can exchange a certain amount of empty bottles to a full bottle.
# the returned number is the amount of bottles drank

def numWaterBottles(self, numBottles: int, numExchange: int) -> int:
    
    drank = numBottles # we start out by drinking them all

    while numExchange <= numBottles: # we can execute the loop that exchanges and drinks bottles a certain amount of times.
        numBottles -= numExchange - 1  # we the exchanged bottles, but gain a bottle.
        drank += 1
    return drank

bottles = 15
exchanges = 4


print(numWaterBottles(0,bottles,exchanges))


# there is also a solution that can solve it with one pass.
# since it is actually a geometric sum it has some limits when passing through each iteration.


def numWaterBottles(self, numBottles: int, numExchange: int) -> int:

    return int((numBottles + ((numBottles - 1)/(numExchange-1))))

# this follows the mathematical formula, so it can pass in O(1) time 