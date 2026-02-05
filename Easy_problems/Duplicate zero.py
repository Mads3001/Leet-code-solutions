

def duplicateZeros(self, arr: list[int]) -> None:
    """
    Do not return anything, modify arr in-place instead.
    """
    # a very easy method could just be reconstructing the list, but duplicating the zeroes. This is probably the fastest.
    new_arr = []
    i = 0
    while len(new_arr) < len(arr): # this loop works until the list has as many elements as the original
        new_arr.append(arr[i])
        if arr[i] == 0 and len(new_arr) < len(arr):
            new_arr.append(0)
        i += 1
        
    arr[:] = new_arr # this replaces everything in the called list. It does that, since it takes and replaces each element in the list.
    # this constructs and replaces the array list. It's practically the same and can be more effective, but not exactly what's asked of.

# this is a fast solution. Other fast solutions have a method where they scan for the amount of zeroes in the string, so it stops after having scanned a certain amount of zeroes.

arr_input = [1,0,2,3,0,4,5,0]

print(duplicateZeros(0, arr_input), arr_input)


# the intended solution is to use .insert("index", "value")

def duplicateZeros(self, arr: list[int]) -> None:
        i = 0 # this is the amount of scanned elements.
        length = len(arr)
        
        

       
        
        while i <length: # this loop is active until an amount equal to the length of the input has been scanned
            if arr[i]==0: # this checks, if the given value is a zero.
                
                arr.insert(i+1,0) # this inserts a 0 in the index after the spotted zero and adds a scanned length to i.
                
                i+=1 # the zero spotted is also a scanned element.
                arr.pop() # since a new object has been inserted the end of the list needs to be cut.
            i+=1 # if it isn't a zero it is simply just a scanned element.