import time
t=time

#-----------
#Big-O  
keys_generator1 = range(1,6) #[1,5]
array1 = list(keys_generator1)
keys_values = ["First", "Secound", "Third", "Fourth", "Fifth"]
dict1 = {}
for i in keys_generator1:
        dict1[i] = keys_values[i-1]

#------O(1) constant complexity
print(f"O(1): First: {array1[0]}")


#-------O(n) linear complexity
for i in array1:
    print(f"         {array1[i-1]}\n {dict1[i].upper()}-----Number of the array O({i})------------ \n         {i}\n")


# print(dict1)
# print(array1)

#------O(n^2) Quadratic complexity - Nested Loops or mapping in matrix/nested list
print("O(n^2)")
X = [[12,7,3],
    [4 ,5,6],
    [7 ,8,9]]

Y = [[5,8,1],
    [6,7,3],
    [4,5,9]]

result = [[0,0,0],
         [0,0,0],
         [0,0,0]]

# iterate through rows
for i in range(len(X)):
   # iterate through columns
   for j in range(len(X[i])):
       result[i][j] = X[i][j] + Y[i][j]
"""
result = [
    [17, 15, 4],
    [10, 12, 9],
    [11, 13, 18]
    ]
"""
print(result)
for r in result:
   print(r)


#-----O(log n)
#most commonly BINARY [LOG_2(8)=3]
#INFO: https://towardsdatascience.com/logarithms-exponents-in-complexity-analysis-b8071979e847


#-----O(2^n) -> O(e^n) exponential OPPOSITE TO LOGARITMIC
#BAD



"""
LINEAR SEARCH:
O(n)
Iterate trought an array using "for loop" in order to find some number (It can be the last and the complexity could be expensive)
Use Logaritmic complexity
BINARY SEARCH
O(log n)
More scaleble throught cuting in pieces the arrays of data


insert and delete for i in list: append(el)/pop(el) -> O(n)

"""

def binary_search_recursive(arr, low, high, x):
 
    # Check base case
    if high >= low:
 
        mid = (high + low) // 2
 
        # If element is present at the middle itself
        if arr[mid] == x:
            return mid
 
        # If element is smaller than mid, then it can only
        # be present in left subarray
        elif arr[mid] > x:
            return binary_search_recursive(arr, low, mid - 1, x)
 
        # Else the element can only be present in right subarray
        else:
            return binary_search_recursive(arr, mid + 1, high, x)
 
    else:
        # Element is not present in the array 
        return -1
 
# Test array
arr = [ 2, 3, 4, 10, 40 ]
x = 10
 
# Function call
result = binary_search_recursive(arr, 0, len(arr)-1, x)
 
if result != -1:
    print("Element is present at index", str(result))
else:
    print("Element is not present in array")  


#Binary Search:
def binary_search(arr, x):
    low = 0
    high = len(arr) - 1
    mid = 0

    while low <= high:

        mid = (high + low) // 2

# If x is greater, ignore left half
        if arr[mid] < x:
            low = mid + 1
# If x is smaller, ignore right half
        elif arr[mid] > x:
            high = mid - 1
# means x is present at mid
        else:
            return mid
# If we reach here, then the element was not present
    return -1

# Test array
arr = [ 2, 3, 4, 10, 40 ]
x = 10

# Function call
result = binary_search(arr, x)

if result != -1:
    print("Element is present at index", str(result))
else:
    print("Element is not present in array")



"""
TIME COMPLEXITY -- RUN TIME USAGE
SPACE COMPLEXITY -- MEMORY USAGE (preserve memory)
"""

#  EDITED IN GIT.DEV and COMMITED/MERGED
