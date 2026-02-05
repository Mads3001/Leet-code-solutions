# we start with an amount of full water bottles.
# we can drink those and turn them empty. 
# we can exchange a certain amount of empty bottles to a full bottle.
# the returned number is the amount of bottles drank
# after each bottle we exchange the amount needed to exchange a bottle goes up by one.




def maxBottlesDrunk(self, numBottles: int, numExchange: int) -> int:
    
    drank = numBottles # we start out by drinking them all

    while numExchange <= numBottles: # we can execute the loop that exchanges and drinks bottles a certain amount of times.
        numBottles -= numExchange - 1  # we the exchanged bottles, but gain a bottle.
        drank += 1
        numExchange += 1 # it also increases by one now.
    return drank

# this solution is somehow very slow.
# it is leetcode being weird again and differing the time for no reason at all


# the fastest solution uses a math formula


def maxBottlesDrunk(self, numBottles: int, numExchange: int) -> int:
    b, e = numBottles, numExchange
    return int(b + (((-2*e) + 3 + ((4*e*e + 8*b - 12*e + 1))** 0.5) / 2))
