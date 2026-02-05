

# this time we just need to return a row of the triangle

"""
def generate(self, numRows: int) -> list[list[int]]:

    # we should be able to do this with a for loop and a for loop.
    triangle = [] # this is the return list

    for _ in range(numRows): # the first row is already given. _ is 1 and 2, if numrows = 3
        # _ is the amount of rows
        tmp_row = [1]
        for i in range(1, _): # the second row will be ignored, since the range is from 0 to 1. the second time i can be 1
            # i is also the amount of elements in a given row.
            tmp_row.append(triangle[_ - 1][i - 1] + triangle[_ - 1][i]) # [_-1] takes values from the last row. [i - 1] starts out by taking the first value of a row. [i] starts with the second value.
            # i goes up to the just under the row number. That means it will take the last value of the last row.
            
        if _:    
            tmp_row.append(1)
        triangle.append(tmp_row)
    return triangle


# let's simulate if numrows = 3
# the thing that caused problems was that i prefilled the first triangle. With that gone the loop goes as planned.
"""
input = 5






    

# this version doesn't store the previous row, since it isn't needed in this case
def getRow(self, rowIndex: int) -> list[int]:

    if rowIndex == 0: # edge case
        return [1]
        
    triangle = [] 

    for _ in range(rowIndex + 1): 
        tmp_row = [1]
        for i in range(1, _): 
            
            tmp_row.append(triangle[i - 1] + triangle[i]) 
        if _:    
            tmp_row.append(1)
        triangle = tmp_row # it can also just replace to use less space.
    return triangle # it should just return the last row

print(getRow(0,input))