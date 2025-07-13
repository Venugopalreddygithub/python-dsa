import array 


my_arr = array.array('i', [1, 2, 3, 4, 5])  # Create an array with initial values

my_arr.remove(1) 
print(my_arr)

""" 
Time complexity & Space complexity:
- Deleting an element: O(n) time, O(1) space.
"""