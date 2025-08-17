from array import array

# Accessing an element from an array using array's index
my_array = array('i', [1, 2, 3, 4])

def acessElement(arr, index):
    if index >= len(arr):
        print("Index does not exist") 
    else:
        print(arr[index])
        
acessElement(my_array, 0)

# Time: O(1)
# Space: O(1)