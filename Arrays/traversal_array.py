from array import array

# Traversal
my_array = array('i', [1, 2, 3, 4])

def traverseArray(arr):
    for index, value in enumerate(arr):
        print(f"Index: {index}, Value: {value}")

traverseArray(my_array)

# Time: O(n) - Linear
# Space: O(1) - Constant