
# this time we will get some strings as layers of lasers in a bank. The lasers at a given layer will all have connections to the lasers in the surrounding layers. 
# The lasers skip empty layers. The code need to return the amount of laser connections active.

# that can easily be done, since the amount of connections between two layers are the amount of lasers at layer 1 times the amount at layer 2 as long as they're not empty.

class Solution:
    def numberOfBeams(self, bank: list[str]) -> int:

        count = 0 # the number of connections

        last_lasers = 0 # the current amount of lasers at the last non-empty floor.

        for layer in bank:
            
            current_lasers = 0
            for cell in layer:
                if cell == "1":
                    current_lasers += 1
            if current_lasers > 0:
                count += last_lasers * current_lasers
                last_lasers = current_lasers
        return count

# the .count can also be used.


class Solution:
    def numberOfBeams(self, bank: list[str]) -> int:

        count = 0 # the number of connections

        last_lasers = 0 # the current amount of lasers at the last non-empty floor.

        for layer in bank:
            
            current_lasers = layer.count("1")

            if current_lasers > 0:
                count += last_lasers * current_lasers
                last_lasers = current_lasers
        return count
    
# .count is builtin and therefore faster.
