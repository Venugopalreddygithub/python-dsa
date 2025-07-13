
import array 

# 1. Create an array with initial values and traverse it 
my_arr = array.array('i', [1, 2, 3, 4, 5, 99, 99])
for i in my_arr:
    print(i, end=' ')

# Time complexity: O(n)
# Space complexity: O(1)

# 2. Access individual elements using indexing
def access_element(arr, index):
    if 0 <= index < len(arr):
        return arr[index]
    else:
        raise IndexError("Index out of bounds")
print(access_element(my_arr, 4))  

# Time complexity: O(1)
# Space complexity: O(1)

# 3. Append any value to the array using append() method
def append_value(arr, value):
    arr.append(value)
    return arr

print(append_value(my_arr, 60))  # Append value 6 to the array

# Time complexity: O(1)
# Space complexity: O(1)

# 4. Insert a value at a specific index using insert() method
def insert_value(arr, index, value):
    if 0 <= index < len(arr):
        arr.insert(index, value)
        return arr
    else:
        raise IndexError("Index out of bounds") 

# print(insert_value(my_arr, 0, 0))

# 5. Extend python array using extend() method
def extend_arr(arr, iterable):
    arr.extend(iterable)
    return arr 

# print(extend_arr(my_arr, [6, 7, 8]))  # Extend the array with new values

# 6. Add items to the array using fromlist() method
def from_list(arr, lst):
    arr.fromlist(lst)
    return arr

# 7.Remove an item from the array using remove() method
def remove_element(arr, value):
    if value in arr:
        arr.remove(value)
        return arr 
    else:
        print(f"Value {value} not found in the array.") 

# print(remove_element(my_arr, 20))

# 8. Remove last array element using pop() method 
def pop(arr, index=-1):
    arr.pop(index)
    return arr  

# 9. Fetch any element through its index using index() method 

# print(my_arr.index(2)) 

# 10. Reverse a array using reverse() method 
# my_arr.reverse()
# print(my_arr)

# 11. Get array buffer information through buffer_info method 
# print(my_arr.buffer_info())

# 12.Check for number of occurances of an element using count() method 
# print(my_arr.count(99))

# 13. convert array to string using toString() method 
# stringArr = my_arr.tobytes()
# arrays = array.array('i', []) 
# arrays.frombytes(stringArr) 
# print(arrays)
# 14.convert to array to list using tolist() 
# print(my_arr.tolist())

# 15.Append a string to char array using fromstring() method 
# char_string = array.array()
# print(char_string)


# 16.Slice elements of an array
# print(my_arr[:-1])

