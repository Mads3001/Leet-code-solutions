
# as input the function will get multiple lists of "classes" The list will constructed as [passing, students]. passing marks the amount of people passing out of students
# the ratio will then be passing/students
# Another input will be a number of students that will pass no matter what. They can be assigned to each class to try and raise the average pass rate.



import heapq

# with a heap, we can keep track of the class with the biggest improvement, when one passing student gets added.
# heap was learnt by a solution, but the rest is selfmade. A heap is a very smart data structure. By default it sorts by lowest amount.
# it can sort by highest, but I need to research how to do that.

def maxAverageRatio(self, classes: list[list[int]], extraStudents: int) -> float:
    
    pq = [] # this is where the heap is stored
    for index, (passing, total) in enumerate(classes):
        current_ratio = passing / total
        new_ratio = (passing + 1) / (total + 1)
        heapq.heappush(pq, (-(new_ratio - current_ratio), index)) # this heap is sorted by the smallest first, so the bigger the difference in percentage gains priority.
        # that is because the gain is set as a negative number. the largest gain is stored as the smallest value.
        # heappush adds an element to the heap. The heap is stored in pq, the value is "-(new_ratio - current_ratio)", and the index is stored.

    # now to distributing extra students
    while extraStudents > 0: # the heap is for deciding which class to add a passing student to, so it then goes and edits the classes list
        gain, index = heapq.heappop(pq) # this removes the smallest value and stores the index and gain.
        passing, total = classes[index] # this opens up the the class with the highest gain. (the index is taken from the line before)
        classes[index][0] += 1 # passing by editing the list
        classes[index][1] += 1 # total by editing the list
        # the passing student is added to the class.
        current_ratio = classes[index][0] / classes[index][1] # a new value needs to be processed for the current ratio
        new_ratio = (classes[index][0] + 1) / (classes[index][1] + 1) # now a new ratio, if there's one more passing person is put in.
        # the new info now needs to be put into the heap
        heapq.heappush(pq, (-(new_ratio - current_ratio), index))
        # the extrastudent count goes down by one
        extraStudents -= 1

    
    # the answer can now be calculated
    cumulative_pass = sum(passing / total for passing, total in classes)
    # this is the cumulative and we just need the average, so it needs to be divided by the amount of classes.
    return cumulative_pass / len(classes)

        




        

students = [[1,2],[3,5],[2,2]]

print(maxAverageRatio(0, students, 2))

