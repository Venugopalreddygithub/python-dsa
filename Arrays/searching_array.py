import array 

def linear_search(arr, target):
    for i in range(len(arr)):
        if arr[i] == target:
            return i  # Return the index of the found element
    return -1  # Return -1 if the element is not found

my_arr = array.array('i', [1, 2, 3, 4, 5])  # Create an array with initial values

print(linear_search(my_arr, 30))

""" 
Time complexity & Space complexity:
- Linear search: O(n) time, O(1) space.
"""