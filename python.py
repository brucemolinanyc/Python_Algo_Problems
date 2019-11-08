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

#TRAVERSING A BINARY TREE
class BST:
    def __init__(self, value):
        self.value = value 
        self.left = None 
        self.right = None
    
    #Average: O(Log(n)) time | O(1) space
    # Worst: O(n) time | O(1) space
    def insert(self, value):
        currentNode = self
        while True:
            if value < currentNode: # then we explore left
                if currentNode.left is None:
                    currentNode.left = BST(value)
                    break
                else: # still have a subtree to explore
                    currentNode = currentNode.left
            else: 
                if currentNode.right is None: # explore right if value > currentNode
                    currentNode.right = BST(value)
                    break 
                else: 
                    currentNode = currentNode.right
        return self

    #Average: O(Log(n)) time | O(1) space
    # Worst: O(n) time | O(1) space
    def contains(self,value):
        currentNode = self
        while currentNode is not None:
            if value < currentNode.value:
                currentNode = currentNode.left
            elif value > currentNode.value:
                currentNode = currentNode.right
            else:
                return True 
        return False 

    def remove(self,value, parentNode=None):
        currentNode = self 
        while currentNode is not None:
            if value < currentNode.value:
                parentNode = currentNode
                currentNode = currentNode.left
            elif value > currentNode.value:
                parentNode = currentNode
                currentNode = currentNode.right
            else: # found our node - the value of currentNode is equal to value we want to remove
                #work with a node that has children nodes - we want to get smallest value of subtree to replace the node removed
                if currentNode.left is not None and currentNode.right is not None:
                    currentNode.value = currentNode.right.getMinValue() #method to get smallest value of right subtree
                    # currentNode.value = smallest value of right subtree
                    currentNode.right.remove(currentNode.value, currentNode)
                # we're gonna come back to the root node case
                elif parentNode is None:
                    if currentNode.left is not None:
                        currentNode.value = currentNode.left.value
                        currentNode.right = currentNode.left.right
                        currentNode.left = currentNode.left.left
                    elif currentNode.right is not None:
                        currentNode.value = currentNode.right.value
                        currentNode.left = currentNode.right.left
                        currentNode.right = currentNode.right.right
                    else: 
                        currentNode.value = None 
                elif parentNode.left == currentNode:
                    parentNode.left = currentNode.left if currentNode.left is not None else currentNode.right
                elif parentNode.right == currentNode:
                    parentNode.right = currentNode.left if currentNode.left is not None else currentNode.right
                break 
        return self 

    def getMinValue(self):
        currentNode = self 
        while currentNode.left is not None:
            currentNode = currentNode.left 
        return currentNode.value 


#Average: O(Log(n)) time| O(Log(n)) space
# Worst: O(n) time | O(n) space

def findClosestValueInBst(tree, target):
    return findClosestValueInBstHelper(tree, target, float("inf"))


# recursive function to traverse the tree in either direction
def findClosestValueInBstHelper(tree, target, closest):
    if tree is None:
        return closest
    if abs(target - closest) > abs(target - tree.value):
        closest = tree.value
    if target < tree.value:
        return findClosestValueInBstHelper(tree.left, target, closest)
    elif target > tree.value:
        return findClosestValueInBstHelper(tree.right, target, closest)
    else: return closest


#iterative method
#Average: O(Log(n)) time| O(1) space
# Worst: O(n) time | O(1) space

def findClosestValueInBst(tree, target):
    return findClosestValueInBstHelper(tree, target, float("inf"))


def findClosestValueInBstHelper(tree, target, closest):
    currentNode = tree 
    while currentNode is not None:
        if abs(target - closest) > abs(target - currentNode.value):
            closest = currentNode.value
        if target < currentNode.value:
            currentNode = currentNode.left
        elif target > currentNode.value:
            currentNode = currentNode.right
        else: # target and currentNode.value are equal
            break
    return closest


print(float("inf"))