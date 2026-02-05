
# we get an array of power. we have a starting position we can freely choose from each iteration. 
# we gather power along the array by absorbing the values. each jump is k long. The maximum possible amount of energy should be returned.
# the jumps of k length should happen until you can't make that jump anymore.


# 2 for loops should be able to make a brute force solution. Dynamic programming is the desired solution, but I do not know enough of it to make that solution.

def maximumEnergy(self, energy: list[int], k: int) -> int:

    highest_energy = 0

    # we start out with a loop that ranges from all starting positions.
    for _ in range(len(energy)):

        gathered_energy = 0 # it needs to start out with the desired start position. it can also be negative, so gathered enery must be small to start out
        i = _
        while i < len(energy): # this takes the other loop and adds power with the jumps of k. it is written, so it stops, if i exceeds the index in the array.
            gathered_energy += energy[i]
            i += k
        if gathered_energy > highest_energy: # reassigns the highest energy.
            highest_energy = gathered_energy
    return highest_energy

# it is not that fast, but very simple. It might time out due to time constraints.

# it timed out...


# the better solution is:
def maximumEnergy(self, energy: list[int], k: int) -> int:
        n = len(energy)
        dp = [0] * n # this makes a list for each index in the array.
        result = float('-inf') # this makes the everything it will be compared to bigger.
        for i in range(n - 1, -1, -1): # this starts at the secondmost end of the array and ends with the last value. it then goes down by 1 for each step. 
            dp[i] = energy[i] + (dp[i + k] if i + k < n else 0) # this way the it keeps track of the maximum amount of energy that can bed stored by starting at the back.
            # for figuring out the earlier indices it just looks at the last indice in the track of k jumps. The maximum value for the last indice is already calculated.
            # then it just needs to add the new indice to the new point.
            result = max(result, dp[i]) # for each new indice it just checks, if it is bigger than the previous max.
        return result
# this solution is insanely smart and goes over each element only once instead of it being exponential (like in my case) this is instead linear.
# i really need to learn to write dynamic programming like this.
