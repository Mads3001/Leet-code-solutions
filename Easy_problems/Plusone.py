
# a number is instead stored in a list
def plusOne(self, digits: list[int]) -> list[int]:
    # it needs to handle, if the last digit is 9 and potentially more of the last digits are nine.

    i = -1
    
    while digits[i] == 9: # this checks and puts up the loop, if nine is the last digit.
        digits[i] = 0 # reassigns the value 
        i -=1 # it is now the second last element that is checked.
        if abs(i) > len(digits): # if i becomes out of the index, then we know a 1 needs to be inserted.
            digits.insert(0,1)
            return digits # if all are nines, then it has then now been

    digits[i] += 1 # this adds a number either after all the nines or at the end of the number
    # the code is not functional, if the largest digit is nine, because the code then need to add another index.
    return digits

# input = [1,2,3]
# input = [4,3,2,1]
input = [1,2,9]
print(plusOne(0, input))