
# this problem states, that 1 person starts out by knowing a secret. 
# The person who knows a secret spreads the secret to another person every "delay" days.
# a person forgets the secret after "forget" days. A person can share the secret multiple times.
# A person doesn't share the secret the day they forget and afterwards.
# n is the amount of days the simulation runs.
# the output needs to be the amount of people who know the secret at the end of day n.

def peopleAwareOfSecret(self, n: int, delay: int, forget: int) -> int:
    day = 1
    # we can set the loop up by using a while.
     # know marks the amount of days someone has known the secret.
    # to keep track of how many people knows and doesn't we can set a list to keep track.
    tell = [1] # the list will have the amount of people who will tell in a certain day.

    # it could make sense to make it a list with a length determined by the forget. Every time someone forgets it loops around and erases the old people who know from that time.
    while  day < n:
        tell[(day % forget)] # this makes the list have a maximum of forget elements.
        # tell[(day % forget) + 1] marks how far in the forget cycle it is. They will add to how many people will tell in this amount of days after the delay.
        # the code is currently not adding enough people, since people from different days can tell on the same day, if they haven't forgotten the secret.
        tell[((day + delay) % forget)]
        # they will tell at this next day. They should then overwrite the old value because those people are forgetting.

        # the right is how many people are going to tell in that certain day-
        # Maybe we should make a list of how many will tell that day.


        day += 1 




day = 0
n = 10
forget = 5

tell = [x for x in range(forget)] # this constructs the list

tell[0] = 1 # day 0 is instead day one.

while  day < n:
    tell[day % forget] = 1 # this is how many will tell this day
    # this will get more complicated, when the delay is taken into consideration.
    # i can think of a solution, but can't express it in code sadly.

    day += 1

print(tell)

# one of the solutions is to make a list with each age. The people with delay % age == 0 will add their amount to day zero.
# if the age is forget, then it is set to zero and excluded from adding to day zero. 
# Then at last every index is shifted to the right to make place for a new day zero. This works fine. The best solution is the dynamic programming approach. I just can't do that one.

# the solution from the internet:
def peopleAwareOfSecret(self, n: int, delay: int, forget: int) -> int:
    dp = [0] * n
    dp[0] = 1
    total = 0
    mod = 10**9 + 7
    for i in range(delay, n):
        total += dp[i - delay]
        dp[i] = total
        if i - forget + 1 >= 0:
            total -= dp[i - forget + 1]
    return (sum(dp[-forget:])) % mod 