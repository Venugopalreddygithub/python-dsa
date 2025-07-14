import numpy as np 

my_arr = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
# print(my_arr)

# Insertion
newArr = np.insert(my_arr, 2, [[10, 20, 30]], axis=0) 
# print(newArr)

# Time complexity: o(mn)

# Accessing element in two dimeninal array
# print(my_arr[0][4])
# Time complexity: O(1) , space: O(1)

# Traverse & searching
rows = len(my_arr) 
cols = len(my_arr[0])

for i in range(rows):
    for j in range(cols):
        # print(my_arr[i][j])  
        if my_arr[i][j] == 30:
            print('Element present')
# Time complexity: O(mn), space: O(1)

# Deletion
print(my_arr)
newArray = np.delete(my_arr, 0, axis=1)
print(newArray)