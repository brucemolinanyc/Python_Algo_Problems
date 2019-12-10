#construction of a BST - making a BST
class BST:
    #initialize a BST
    def __init__(self, value):
        self.value = value 
        self.left = None 
        self.right = None 

    def append(self, value):
        currentNode = self 
        while True: # traverse the tree
            if value < currentNode.value: # if its less, we're going to the left
                if currentNode.left is None: #we've reached the end of the tree and can add the new value
                    currentNode.left = BST(value )
                    break 
                else: 
                    currentNode = currentNode.left 
            else:
                if value > currentNode.value:
                    if currentNode.right is None:
                        currentNode.right = BST(value)
                        break
                    else: 
                        currentNode = currentNode.right 
        return self 


    def contains(self, value):
        currentNode = self 
        while currentNode is not None:
            if value < currentNode.value: #if its less than, we'll keep exploring the left side
                currentNode = currentNode.left 
            elif value > currentNode.value: # if its greater than, we'll explore the right side
                currentNode = currentNode.right 
            else: # if its not less than or greater than, it can only be equal - we found a match
                return True 
        return False # if we wind up at the bottom of a tree with no match, its False












    # def __init__(self,value):
    #     self.value = value
    #     self.left = None
    #     self.right = None 


    # def insert(self, value):
    #     currentNode = self 
    #     while True: # traverse the tree
    #         if value < currentNode.value: # if its less, we're going to the left
    #             if currentNode.left is None: #we've reached the end of the tree and can add the new value
    #                 currentNode.left = BST(value )
    #                 break 
    #             else: 
    #                 currentNode = currentNode.left 
    #         else:
    #             if value > currentNode.value:
    #                 if currentNode.right is None:
    #                     currentNode.right = BST(value)
    #                     break
    #                 else: 
    #                     currentNode = currentNode.right 
    #     return self 


        

    # def contains(self, value):
    #     currentNode = self 
    #     while currentNode is not None:
    #         if value < currentNode.value: #if its less than, we'll keep exploring the left side
    #             currentNode = currentNode.left 
    #         elif value > currentNode.value: # if its greater than, we'll explore the right side
    #             currentNode = currentNode.right 
    #         else: # if its not less than or greater than, it can only be equal - we found a match
    #             return True 
    #     return False # if we wind up at the bottom of a tree with no match, its False



