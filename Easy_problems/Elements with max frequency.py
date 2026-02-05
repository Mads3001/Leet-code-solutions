
# the code takes an input of a list and should return the element that is most frequent in the list


def maxFrequencyElements(self, nums: list[int]) -> int:
    frequency_map = {}
    

    for number in nums:
        frequency_map[number] = 1 + frequency_map.get(number, 0)
    
    frequency_list = list(frequency_map.values())
    frequency_list.sort()

    numbers_with_max_frequency = frequency_list[-1]
    if len(frequency_list) > 1:
        for _ in range(1, len(frequency_list)):
            if frequency_list[-_] == frequency_list [-(_ + 1)]:
                numbers_with_max_frequency += frequency_list [-(_ + 1)]
            else:
                break
    

    return numbers_with_max_frequency



# this solution is very memory effective, but quite slow.

# a faster solutiuon could keep track, of the maximum frequency and update the total amount of number having the maximum frequency
# this method is faster, since the first solution could become quite slow when sorting a very long list.

def maxFrequencyElements(self, nums: list[int]) -> int:
    frequency_map = {}
    
    max_frequency = 0
    numbers_at_maxfrequency = 0

    for number in nums:
        frequency_map[number] = 1 + frequency_map.get(number, 0)

        if frequency_map.get(number, 0) == max_frequency:
            numbers_at_maxfrequency += frequency_map.get(number, 0)
        
        if frequency_map.get(number, 0) > max_frequency:
            max_frequency = frequency_map.get(number, 0)
            numbers_at_maxfrequency = max_frequency


    return numbers_at_maxfrequency

numbers = [1,2,2,3,1,4]
print(maxFrequencyElements(0, numbers))