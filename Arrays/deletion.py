from array import array

# Deletion
my_array = array('i', [1, 2, 3, 4])

print(my_array)
print(my_array.pop(0))
print(my_array)

# Time: O(n)
# Space: O(1)