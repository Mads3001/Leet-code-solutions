
# this function should check, if a number is a palindrome


def isPalindrome(self, x: int) -> bool:

    for i in range(len(str(x))):
        if str(x)[-(i + 1)] != str(x)[i]:
            return False
    return True


# this function is just quite slow

def isPalindrome(self, x: int) -> bool:
    # we need to create the reverse of x
    # we can do that, if it is a string.
    # we just need to remove the plus or minus in the value
    num = str(x)
    reverse_num = num[::-1] # this will take and subscribt from the end to the start. It works since suscribting follows:
    # start_pos : end_pos : step_size. You could change the step size, so it only subscribts every second character.
    # this case works, since an empty input means, it is 0 to 0. It starts with 0 and loops back to 0 in terms of normal subscribting.
    if num == reverse_num:
        return True
    return False

print(isPalindrome(0, 121))




