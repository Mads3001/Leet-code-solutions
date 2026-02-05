def numberOfSteps(self, num: int) -> int:
        steps = 0
        while num > 0:
            if not num % 2:
                num /= 2
                steps += 1
            else:
                num -= 1
                steps += 1

        return steps