
# this time the word order is preserved, but the letters in each word are reversed.


class Solution:
    def reverseWords(self, s: str) -> str:

        words = s.split()

        for i, word in enumerate(words):
            words[i] = word[::-1] # reverse the letters

        return " ".join(words)