# from datetime import datetime

# def binarySearch(arr, item):
#     low = 0
#     high = len(arr) - 1 
#     while low <= high:
#         mid = low + high
#         guess = arr[mid]
#         if guess == item:
#             return mid
#         if guess > item:
#             high -=1
#         else:
#             mid += 1
#     return None 


# def binarySearch(arr, item):
#     low = 0
#     high = len(arr)-1

#     while low < high:
#         mid = low + high 
#         if arr[mid] == item:
#             return mid
#         if arr[mid] > item:
#             high -= 1
#         if arr[mid] < item:
#             low += 1
#     return "not present"


#RECURSIVE

# def binarySearch(array, target):
#     return binarySearchHelper(array, target, 0, len(array)-1)

# def binarySearchHelper(array,target, left, right):
#     if left > right:
#         return -1
#     middle = (left + right)//2
#     potentialMatch = array[middle]
#     if target == potentialMatch:
#         return middle
#     elif target < potentialMatch:
#         return binarySearchHelper(array, target, left, middle - 1)
#     else:
#         return binarySearchHelper(array, target, middle + 1, right )


#my recursive
def binarySearch(arr, target):
    return binarySearchHelper(arr, target, 0, len(arr) - 1)


# def binarySearchHelper(arr, target, left, right):
#     if left > right:
#         return - 1 
#     middle = (left + right) // 2 
#     potentialMatch = arr[middle]
#     if potentialMatch == target:
#         return middle 
#     if potentialMatch < target:
#         return binarySearchHelper(arr, target, middle + 1, right)
#     else:
#         return binarySearchHelper(arr, target, left, middle - 1)
 

# ITERATIVE
# def binarySearch(arr, target):
#     left = 0
#     right = len(arr) - 1
#     while left <= right: 
#         middle = (left + right) // 2 
#         potentialMatch = arr[middle]
#         if potentialMatch == target:
#             return middle 
#         if potentialMatch < target:
#             left = middle + 1 
#         else:
#             right = middle - 1
#     return -1


#iterative

# def binarySearch(arr, target):
#     left = 0 
#     right = len(arr) - 1 
#     while left <= right:
#         middle = (left + right) // 2 
#         possibleMatch = arr[middle]
#         if possibleMatch == target:
#             return middle
#         if possibleMatch > target:
#             right = middle - 1 
#         else:
#             left = middle + 1 
#     return -1

# recursive
def binarySearch(arr, target):
    return binarySearchHelper( arr, target, 0, len(arr)-1 )

def binarySearchHelper(arr,target, left,right):
    middle = (left + right) // 2 
    possibleTarget = arr[middle]
    while left <= right:
        if possibleTarget == target:
            return middle 
        if possibleTarget > target:
            return binarySearchHelper(arr, target, left, middle - 1)
        if possibleTarget < target:
            return binarySearchHelper(arr, target, middle + 1, right)
    return -1

my_list = [1, 3, 5, 7, 9,10,11,12,13,23,55,66,77]
print (binarySearch(my_list, 77))