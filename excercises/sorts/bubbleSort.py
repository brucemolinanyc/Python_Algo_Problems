def bubbleSort(arr):
    isSorted = False 
    counter = 0 
    while not isSorted:
        isSorted = True 
        for i in range(len(arr)-1-counter):
            if arr[i] > arr[i+1]:
                arr[i+1], arr[i] = arr[i], arr[i+1]
                isSorted = False
        counter += 1
    return arr 
 
print(bubbleSort([33,2,1,31,78,4,5,100,6,7]))