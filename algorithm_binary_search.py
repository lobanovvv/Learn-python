#Binary search algorithm
import math

arr = [12, 15, 22, 28, 35, 54, 61, 82]

def binSearch(array, key):

    middle = math.floor(len(arr) / 2) - 1

    if arr[middle] == key:
        return middle
    elif arr[middle] > key:
        minEdge = arr[0]
        maxEdge = arr[middle - 1]
        middle = math.floor(maxEdge - minEdge / 2)

    return -1


x = binSearch(arr, 28)
print(x)
print( math.floor(len(arr) / 2))