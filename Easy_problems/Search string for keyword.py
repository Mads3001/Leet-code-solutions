


# this function should search a string for occurences of a smaller string.

def strStr(self, haystack: str, needle: str) -> int:
    
    length = len(needle)
    if length > len(haystack): # if the needle is greater than the haystack
        return -1

    _ = 0
    while _ < len(haystack):
        if haystack[_] == needle[0]: # if the first letter is present, then it should check for the following letters to also be correct
            if _ + length > len(haystack): # if the length of the needle would exceed the index of the haystack it is not possible.
                break # now the code is protected from indexerror.
            for i in range(0,length):
                if haystack[_ + i] != needle[i]:
                    break
                if i == length - 1:
                    return _
        _ += 1
    return -1


big = "fhdvjnbkjbdjksfio"

small = "ios"

print(strStr(0,big,small))