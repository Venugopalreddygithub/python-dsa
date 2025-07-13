import array 

def traverse(arr):
    for i in arr:
        print(i)

my_array = array.array('i', [1, 2, 3, 4, 5]) 
print("Original array:", my_array)

my_array.insert(5, 6)  # Insert 6
print("After inserting 6:", my_array)

""" 
Time complexity & Space complexity:
- Inserting an element: O(n) time, O(1) space.
"""

""" 
Time complexity & Space complexity:
- Traversing an array: O(n) time, O(1) space.
"""