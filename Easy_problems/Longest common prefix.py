
# this code should just find the longest common prefix in an array of strings.

def longestCommonPrefix(self, strs: list[str]) -> str:

    # the longest prefix can only be as long as the shortest word.

    # I should make a while loop with a for loop inside.

    shortest_word = min(len(x) for x in strs)
    i = 0 # i is the index.
    common_prefix = ""
    while i < shortest_word:
        for word in strs:
            if word[i] != strs[0][i]: # this just checks if the word has the same letter as the other. if not, then it should break and return
                return common_prefix
        common_prefix += strs[0][i]
        i += 1
    return common_prefix
    


