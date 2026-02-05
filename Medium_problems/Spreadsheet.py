
# the code should generate a spreadsheet with collumns from A to Z. The amount of rows is customized. It needs to be interactive.


# Uppercase letters: A-Z: ASCII 65–90
# chr() bruges til at decode ASCII til bogstaver.

class Spreadsheet:

    def __init__(self, rows: int): # this is executed, when there is no ."function" applied. The input is then seen as rows 
        # We can store the data in a hash map. The key is the name A to Z and the value is stored in the key value.
        self.spreadsheet = {}
        for r in range(1, rows + 1): # The outer loop makes the rows
            for _ in range(65, 91): # This loop initializes the hash map from A to Z and all the values to 0. Now it needs to to create rows. That can be done with an outer loop
                self.spreadsheet[chr(_) + f"{r}"] = 0

    def setCell(self, cell: str, value: int) -> None: # sets a cell to a certain value.
        self.spreadsheet[cell] = value

    def resetCell(self, cell: str) -> None: # just sets a cell to zero.
        self.spreadsheet[cell] = 0

    def getValue(self, formula: str) -> int: # this is suddenly more complex. It needs to execute normally, when no key from the spreadsheet is mentioned.
        # since the form is always "=x+y" we ned to be able to find x and y. Therafter we need to assess, if it is a cell or an integer.
        # some code that can find the + and split up x and y. They can both be tested, if they're 
        parts = formula[1:].split('+')
        # parts is now a list with two strings.
        if parts[0].isdigit() and parts[1].isdigit(): # if both are digits
            return (int(parts[0]) + int(parts[1]))
        if parts[0].isdigit():
            return (int(self.spreadsheet[parts[1]]) + int(parts[0])) # if only the first is a digit
        if parts[1].isdigit():
            return (int(self.spreadsheet[parts[0]]) + int(parts[1])) # if only the second is a digit
        # both are a cell, if it reaching this point.
        return (int(self.spreadsheet[parts[0]]) + int(self.spreadsheet[parts[1]]))
        

# the code is very slow, since this actually makes a list that large. Other people make it only initialize the needed cells.        


# Your Spreadsheet object will be instantiated and called as such:
# obj = Spreadsheet(rows)
# obj.setCell(cell,value)
# obj.resetCell(cell)
# param_3 = obj.getValue(formula)

# the faster code that works, but technically does not do it the intended way is:


class Spreadsheet:

    def __init__(self, rows: int):
        self.rows = rows
        self.cells = {}

    def setCell(self, cell: str, value: int) -> None:
        self.cells[cell] = value

    def resetCell(self, cell: str) -> None:
        self.cells.pop(cell, None)

    def getValue(self, formula: str) -> int:
        parts = formula[1:].split('+')
        return sum(int(p) if p.isdigit() else self.cells.get(p, 0) for p in parts)