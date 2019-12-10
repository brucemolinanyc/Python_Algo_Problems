def findThreeLargestNumbers(array):
    return sorted(array)[-3:]

def bubbleSort(array):
    isSorted = False 
    counter = 0 
    while not isSorted:
        isSorted = True 
        for i in range(len(array)-1-counter):
            if array[i] > array[i+1]:
                array[i], array[i+1] = array[i+1], array[i]
                isSorted = False 
        counter += 1
    return array 

def findThreeLargestNumbers(array):
    sortedArray = bubbleSort(array)
    return sortedArray[-3:]

def insertionSort(array):
    for i in range(1, len(array)):
        j = i 
        while j > 0 and array[j] < array[j-1]:
            array[j], array[j-1] = array[j-1], array[j]
            j -= 1
    return array

def findThreeLargestNumbers(array):
    #sort the array first - not using a sort method but 
    #the insertion sort algo
    sortedArray = insertionSort(array)
    return sortedArray[-3:]


print(findThreeLargestNumbers([55,43,11,3,-1,10]))
