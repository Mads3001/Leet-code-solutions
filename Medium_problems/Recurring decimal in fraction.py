

# the code needs to find infinitely repeating patterns when dividing.
# that can be done, if the remainder keeps being the same when doing manual long division.
# a hashmap can be used to map all the remainders. 

def fractionToDecimal(self, numerator: int, denominator: int) -> str:
    if numerator == 0: # if the top is zero, then it can only be zero.
        return "0"
    
    fraction = []
    if (numerator < 0) ^ (denominator < 0): # this checks, if any of the numbers are negative.
        fraction.append("-")

    dividend = abs(numerator) # if it is negative or positive have been handled 
    divisor = abs(denominator)
    fraction.append(str(dividend // divisor)) # this stores the whole number. 
    remainder = dividend % divisor # this stores the remainder of long division
    if remainder == 0: # if it is zero, then it can be divided evenly into whole numbers
        return "".join(fraction) # you then just return the fraction as a string. (it was a list before)

    fraction.append(".") # if it isn't a whole number, then a decimal point is added.
    map_dict = {}
    while remainder != 0: 
        if remainder in map_dict: # if the remainder have been seen before, then the final number is constructed as infinitely repeating.
            fraction.insert(map_dict[remainder], "(")
            fraction.append(")")
            break
        map_dict[remainder] = len(fraction) # the rest of the loop makes the long division.
        remainder *= 10
        fraction.append(str(remainder // divisor))
        remainder %= divisor

    return "".join(fraction)