
# the code should take two strings with binary numbers and combine add them. The output should also be a binary number


def addBinary(self, a: str, b: str) -> str:

    # since they are strings we could just start out by adding from the end of the strings.
    # we can reverse them
    al = list(a)
    bl = list(b)
    al.reverse()
    bl.reverse()

    if len(al) >= len(bl):
        ma_length = (len(al), al)
        mi_length = (len(bl), bl)
    if len(bl) > len(al):
        ma_length = (len(bl), bl)
        mi_length = (len(al), al)
    # we need to figure out the length of both.
    # the result can be stored in an array and be joined.
    result = []
    # there should be a loop that marks if the binary chain of 1 should extend the number. almost like 10's in normal numbers.
    i = 0
    carry = 0
    while i < mi_length[0]:
        # a better approach could be adding the elements and deciding from there.
        bit_sum = int(al[i]) + int(bl[i]) + carry
        result.append(str(bit_sum % 2))
        carry = bit_sum // 2
        i += 1


    # now we just need to go over the rest of the number.

    for i in range(mi_length[0], ma_length[0]): # this will then look at the rest of the elements.
        if carry:
            if ma_length[1][i] == "0":
                result.append("1")
                carry = False
            else:
                result.append("0")
        else:
            result.append(ma_length[1][i])
    if carry:
        result.append("1")
    result = "".join(result)
    
    return result[::-1]





def add_binary_strings(a, b):
    # Pad shorter string with leading zeros
    max_len = max(len(a), len(b))
    a = a.zfill(max_len)
    b = b.zfill(max_len)

    carry = 0
    result = []

    for i in range(max_len - 1, -1, -1):
        bit_sum = int(a[i]) + int(b[i]) + carry
        result.append(str(bit_sum % 2))  # Append string '0' or '1' # this time we just check for even or uneven.
        carry = bit_sum // 2

    if carry:
        result.append('1')

    return ''.join(result[::-1])