def search(arr, n, x):
    # loop through all elements
    for i in range(n):
        if arr[i] == x:    # if element matches
            return i       # return index
        
    # if element not found
    return -1

# array to search
arr = [2, 3, 4, 10, 40]

#element to find
x = 10

#length of array
n = len(arr)

#function call
result = search(arr, n, x)

#output result
if result == -1:
    print("element is not present in array")
else:
    print("element is present at index", result)    