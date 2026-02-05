
def canConstruct(self, ransomNote: str, magazine: str) -> bool:

    if len(magazine) < len(ransomNote):
        return False
        # if the total amount of letters in maga_hash is less than in the ransomnote, then it can't physically be crafted. 


    maga_hash = {} # for this problem we need to create a maga hash. It is a map that can store a pair of data values. In this case we need one string and an integer.
    # the left value is called a key and the right one is the value.
    # a dictionary cannot have duplicate keys. There can only exist one of each key. There cannot be two keys named Y and have different values. 

    for character in magazine:
        maga_hash[character] = 1 + maga_hash.get(character, 0) # maga_hash named for the variable character will now contain the character and an integer.
        # maga_hash[character] initializes the key for "character". It is equal to the value. "maga_hash.get(x, y)" returns the value for "character" because of .get
        # the equation initializes the value to 0, but the first time a character shows up the value will change to 1 and go up by one for each subsequent time it's discovered.



    for character in ransomNote:
        if character not in maga_hash or maga_hash[character] <= 0: # this checks, if the character is in the dictionary. Or if the value of the character is negative.
            # if negative, then the character is used up.
            return False # if those are true, then there's missing characters for the ransom note.
        maga_hash[character] -= 1 # if the letter is in the dictionary and there's a positive amount, then one letter will be used up and removed from the library

    return True # if the character in ransomnote loop finishes, then all the letters are in the magazine.


ransom = "aaaabbbbbdfghddd"

mag = "aaaabbbbbdfghlddddasgwedveewgf"

if canConstruct(0 , ransom, mag):
    print(True)




