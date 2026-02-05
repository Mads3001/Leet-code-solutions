


def areaOfMaxDiagonal(self, dimensions: list[list[int]]) -> int:   # checks for the largest diagonal and then returns the largest area of the triangle with the largest diagonal
        largest_area = 0
        largest_diagonal = 0
        for triangle in dimensions: # for loop that calculates the diagonal
            area = 0
            diagonal = (triangle[0] * triangle[0] + triangle[1] * triangle[1]) # this is equivalebt to a^2+b^2=c^2. The square root is skipped, since it will not make a difference in the decision of the largest diagonal. Furtheremore it also makes the system not prone to floating point errors.
            if diagonal == largest_diagonal: # if the diagonal is equal to the largest, then the largest area is stored.
                    area = triangle[0] * triangle[1]
                    if area >= largest_area: # if the are now is larger, then the new largest area get stored
                        largest_area = area
            if diagonal > largest_diagonal: # check against the largest diagonal length
                largest_diagonal = diagonal # the new value is stored
                area = triangle[0] * triangle[1]
                largest_area = area # this is now the largest area with the largest diagonal
            
        return largest_area