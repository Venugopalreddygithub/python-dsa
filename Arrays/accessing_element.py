import array 

my_arr = array.array('i', [1, 2, 3, 4, 5]) # Create an array with initial values

def access_element(arr, index):
    if 0 <= index < len(arr):
        return arr[index]
    else:
        raise IndexError("Index out of bounds") 

print(my_arr[50])

""" 
Time complexity & Space complexity:
- Accessing an element: O(1) time, O(1) space.
"""