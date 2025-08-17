from array import array
# 1. create an array and traverse.

my_array = array('i', [1, 2, 3, 4])
# for i in my_array:
#     print(i) 
    
# Time: O(n), Space: O(1)
    
# 2. Access individual elements through indexes 
def acess_elemnt(arr: list[int], index: int):
    if index >= len(arr):
        print("Index out of range") 
    else:
        print(arr[index])
    # Time: O(1), Space: O(1)

# acess_elemnt(my_array, 4) 

# 3. Append any value to the array using append() method
def append_value(arr, value):
    arr.append(value)
    print(arr)
# append_value(my_array, 5)
# Time: O(1), Space: O(1)

# 4.Insert value in an array using insert() method 
def insert_value(arr, index, value):
    arr.insert(index, value) 
    print(arr) 

# insert_value(my_array, 10, 100)
# Time: O(n), Space: O(1)

# 5. Extend python array using extend() method 
# my_array.extend([10, 20, 30, 40]) 
# print(my_array)
# Time: O(k), Space: O(k)

# 6.Add items from list into array using fromlist() method 
# my_array.fromlist([100, 200, 300]) 
# print(my_array)
# Time: O(k), Space: O(k)

# 7.Remove an element using remove() method 
# my_array.remove(1)
# print(my_array)
# Time: O(n), Space: O(1)

# 8.Remove last element using pop() method 
def pop_elemnt(arr):
    if arr != []:  
        my_array.pop() 
    return arr
# print(pop_elemnt(my_array))
# Time: O(1), Space: O(1)

# 9.Fetch any element through its index using index() method 
def fetch_element(arr, value):
    return arr.index(value) 
# print(my_array)
# print(fetch_element(my_array, 40))
# Time: O(n), Space: O(1) 

# 10.Reverse a array using reverse() method
# my_array.reverse()
# print(my_array)
# Time: O(n), Space: O(1)

# 11.Get array buffer information using buffer_info() method.

# print(my_array.buffer_info())
# Time: O(1), Space: O(1)

# 12.check for no.of occurance of an element using count() method.
# print(my_array.count(1))
# TIme: O(n), SPace: O(1)

# print(my_array.tolist())
# Time: O(n), Space: O(n)

# 16.Slice elements from an array 
print(my_array)
print(my_array[0:2]) 
print(my_array[2:])
# Time: O(k), Space: O(k)
