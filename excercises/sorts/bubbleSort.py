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

# # def swap(i,j,array):
# #     array[i], array[j] = array[j], array[i]


  


print(bubbleSort([33,2,1,31,78,4,5,100,6,7]))