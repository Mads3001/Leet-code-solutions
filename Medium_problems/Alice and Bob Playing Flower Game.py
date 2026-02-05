# there will be two fields of flowers and two players
# Player 1 is alice and she starts by picking a flower, then player 2, bob, picks a flower, then back to alice and so forth.
# Alice only wins when the number of flowers in total starts out by being uneven.
# The number of flowers in each lane is equal to x and y. X is defined as range(1, x) and y is defined as range(1, y).
# x cannot be equal to y. (that would make the amount of flowers even)
# the function needs to return the amount of all the possible combinations where Alice would win.

def flowerGame(self, n: int, m: int) -> int:
    
    # there can be two scenarios for x and y. One where the x is even and y is uneven and the reverse

    # for the first scenario then every even value for x is valid and every uneven value for y is valid

    even_x = n // 2 # the amount of valid (even) x-values. x and y cannot be zero.
    uneven_y = (m + 1) // 2 # the amount of valid (uneven) y-values.
    # you can arrange the flowers in (even_x)! * (uneven_y)! combinations

    # the first choice has even_x different choices. The second element has uneven_y amount of choices.

    
    uneven_x = (n + 1) // 2
    even_y = m // 2
    # for the second scenario it is the reverse



    winning_times = even_x * uneven_y + uneven_x * even_y

    return winning_times

print(flowerGame(0, 1, 10))