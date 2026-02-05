
# the input will be a string of words with at least one whitespace between each word.

# the solution could be to split all words at the whitespace, then strip the whitespace from the words, then join back the string and add a whitespace in the process.
# at last to remove trailing and leading spaces we just lstrip and rstrip.

class Solution:
    def reverseWords(self, s: str) -> str:

        words = s.split()
        words.reverse()

        return " ".join(words) 
    # the are joint by using the first string argument as the separator. We just use a space in this version
