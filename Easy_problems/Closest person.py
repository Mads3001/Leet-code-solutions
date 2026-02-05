
# the input, x, y and z is given. It is integers and it returns either 1, 2 or 0 depending on, if they reach the person at the same time.

def findClosest(self, x: int, y: int, z: int) -> int:
    # we start by calculating the distance from one of the perons to person 3.
    dist1 = abs(z - x)
    dist2 = abs(z - y)
    if dist1 == dist2: # they both reach at the same time
        return 0
    if dist2 > dist1: # if distance 2 is greater, then person one reaches first
        return 1
    else:
        return 2

# the code should be pretty fast due to having absolutes, subtraction followed by two checks. You can maybe do something smart with bits, but I canøt think of any. 
p1_x = 2
p2_y = 10
p3_z = 6

print(findClosest(0, p1_x, p2_y, p3_z))