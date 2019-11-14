# Depth First Search - Go deep down a branch all the way down before you explore the next branch
# and so on. So Left most branches than inner-left mosts and inner-right mosts
# For every node, we add nodes name to answer array. For every child node, we call DFS function and
# pass in the final array

class Node:
    def __init__(self, name):
        self.children = []
        self.name = name 
    
    def addChild(self, name):
        self.children.append(Node(name))
    
    def depthFirstSearch(self, array):
        array.append(self.name)
        for child in self.children:
            child.depthFirstSearch(array)
        return array

test = Node("A")
test.addChild("B")
print(test, test.children)
# print(test.depthFirstSearch([]))
# test.addChild("B")
# test.addChild("C")
# test.addChild("D")
# test.addChild("L")
# test.addChild("M")

print(test.depthFirstSearch([]))