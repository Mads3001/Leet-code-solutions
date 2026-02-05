
# The function gets a string of words separated by a space and a string of characters on a keyboard that are broken.
# The function should split the string by each space and make it a list. Then a for loop can check if there's any broken characters in the string.

def canBeTypedWords(self, text: str, brokenLetters: str) -> int:

    is_in = False
    words = 0
    for word in text.split():
        is_in = False
        for letter in brokenLetters:
            if letter in word:
                is_in = True
        if not is_in:
            words += 1


    return words

broken = "adl"

txt = "hello world kjfjg hfhkhbv d kjs ajf"

print(canBeTypedWords(0, txt, broken))




# the faster method utilizes a set to make the lookup time faster and not need to have the second for loop as complicated. set is preferred, since it's like a hash map, but only stores the key and not a value.

class Solution:
    def canBeTypedWords(self, text: str, broken: str) -> int:
        brokenKeys = set(broken)
        words = text.split(" ")
        count = 0

        for word in words:
            for c in word:
                if c in brokenKeys:
                    count += 1
                    break

        return len(words) - count