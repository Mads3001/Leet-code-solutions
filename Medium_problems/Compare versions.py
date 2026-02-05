
# two versions are compared to see which one is newer. 
    # If version1 < version2, return -1.
    # If version1 > version2, return 1.
    # Otherwise, return 0.
# leading zeroes should be ignored. for example 1.00001 is the same as 1.1.
# one version can have way more . than the other. eg. 1.0.0.0.0.0.1 and 1.0.0. The left is the newest patch
# we can just split the version number at each .


def compareVersion(self, version1: str, version2: str) -> int:
    versions1 = version1.split(".")
    versions2 = version2.split(".")

    if len(versions1) >= len(versions2):
        min_length = len(versions2)
        max_length = len(versions1)
        longest_version = (versions1, 1) # we use a tuple to store which version is the longest by storing the value that should be returned, if that version is the newest.
    else: 
        min_length = len(versions1)
        max_length = len(versions2)
        longest_version = (versions2, -1)

    i = 0
    while i < min_length: # this checks for for all the shared points of updates.
        if int(versions1[i]) > int(versions2[i]):
            return 1
        if int(versions1[i]) < int(versions2[i]):
            return -1
        i += 1
    
    # another loop that cheks for any value greater than zero in the unshared part of updates.
    while i < max_length:
        if int(longest_version[0][i]) > 0:
            return longest_version[1]
        i += 1
    
    # if all those run through without returning, then it is equal and returns 0
    return 0

# other solutions made the list the same length by just appending zeroes, when one of the versions lacked length. 
# Just by checking against zero instead of appending to a list is probably faster and less memory intensive, when the versions get very long
# no idea why a version number would be that long though



    


        
