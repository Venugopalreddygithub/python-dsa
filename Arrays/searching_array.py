from array import array

# Searching for a target value in array and return it's index otherwise -1
my_array = array('i', [1, 2, 3, 4])
target = 1 

def linear_search(arr, target):
    for index, value in enumerate(arr):
        if value == target:
            return index 
    return -1

print(linear_search(my_array, target))

# Time: O(n) 
# Space: O(1)