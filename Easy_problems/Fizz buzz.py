

class Solution: # this is a method
    def fizzBuzz(self, n: int) -> list[str]:
            fizz_buzz_sequence = [] # The list with the output gets initialized
            for step in range(1, n + 1): # A for loop, that apllies the FizzBuzz filter to all whole values under and including the input "n".

                fizz_or_buzz = "" # FizzBuzz answer gets initialized as an empty string.

                if not step % 3: # Applies Fizz, if divisible by 3.
                    fizz_or_buzz += "Fizz"
                
                if not step % 5: # Applies Buzz, if divisible by 5.
                    fizz_or_buzz += "Buzz"
                
                if not fizz_or_buzz: # If the fizz_or_buzz is still empty, then it is set to be the step value.
                    fizz_or_buzz = str(step) # The output needs to be a string, so it'll be converted.
                
                fizz_buzz_sequence.append(fizz_or_buzz) # The result gets appended (added to end) to the output list.
            return fizz_buzz_sequence # self explanatory    