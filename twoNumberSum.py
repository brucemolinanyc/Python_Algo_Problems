# Two for loop solution - O(n^2) time | O(1) space  -  N represents the length of the array
def twoNumberSum(array, targetSum):
    for i in range(len(array)-1):
        for j in range(i+1, len(array)):
            if array[i] + array[j] == targetSum:
                return sorted([array[i], array[j]])
    return []

#O(n) time | O(n) space because we're storing values in the hash table 
# Hash table is advantageous cuz it uses more space but runs faster and more efficiently
def twoNumberSum(array, targetSum):
    nums = {}
    for num in array:
        potentialMatch = targetSum - num
        print(potentialMatch, nums)
        if potentialMatch in nums:
            print('this one below is right')
            return[potentialMatch, num]
        else:
            nums[num] = True 
    return []

# O(n(Log(n))) time | O(1) space
def twoNumberSum(array, targetSum):
    array.sort()
    left = 0
    right = len(array) - 1
    while left < right:
        currentSum = array[left] + array[right]
        if currentSum == targetSum:
            return sorted([array[left], array[right]])
        elif currentSum < targetSum:
            left += 1
        elif currentSum > targetSum:
            right -= 1
    return []

# print(twoNumberSum([3,5,-4,8,11,1,-1,6], 10))
