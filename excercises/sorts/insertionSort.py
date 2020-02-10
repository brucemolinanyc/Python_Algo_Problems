""" 
Loop backwards through an array to sort the array
"""

def insertionSort(arr):
    for i in range(1, len(arr)):
        j = i 
        while j > 0 and arr[j] < arr[j-1]:
            arr[j-1], arr[j] = arr[j], arr[j-1]
            j -= 1
    return arr 


print(insertionSort([3,2,1,4,5,6,7,5]))
