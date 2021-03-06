# Lists, Trees, Hash Tables, Graphs
# create, insert, search, delete


# Linked List
# The Time Complexity is On - can I skip an element and am I going over anything twice?
# If not it is probably On
# class Node:
#     def __init__(self, num, next):
#         self.num = num
#         self.next = next

#     # implement a length function

#     def len(self):
#         if self.next == None:
#             return 1
#         else:
#             return 1 + self.next.len()
        


# # lets make the length function O1 - always constant - having the same amount of time
# # to get the length of a list of 500 as you would a list of 1 item

# class Node:
#     def __init__(self, num, next):
#         self.num = num
#         self.next = next 
#         if next == None:
#             self.count = 1
#         else:
#             self.count = self.next.count + 1


    


# #Trees 
# #On - every thing is only being iterated on once
# class Node:
#     def __init__(self, num, left, right):
#         self.num = num 
#         self.left = left
#         self.right = right 

#     def len(self):
#         if self == None:
#             return 0
#         elif self.left == None and self.right == None:
#             return 1 
#         else:
#             return 1 + self.left.len() + self.right.len()



# #O1 - Tree
# class Node: 
#     def __init__(self, num, left, right):
#         self.num = num 
#         self.left = left
#         self.right = right 

#         if self.left == None and self.right == None:
#             self.count = 1
#         elif self.left != None and self.right == None:
#             self.count = 1 + self.left.count 
#         elif self.left == None and self.left != None:
#             self.count = 1 + self.right.count 
#         else:
#             self.count = 1 + self.left.count + self.right.count 

#     def len(self):
#         return self.count 





"""Given a string of words with numbers and special characters  
interspersed throughout, remove the special characters and numbers. 
Then print the remaining words in sorted order one word per line."""


# def parser(str):
#     result = []
#     for word in str.split(" "):
#         newWord = ""
#         for char in word:
#             if char.isalpha():
#                 newWord += char
#         if newWord is not "":
#             result.append(newWord)
#     for word in sorted(result):
#         print(word)


def parser(string):
    result = []
    for word in string.split(" "):
        newWord = ""
        for char in word:
            if char.isalpha():
                newWord += char 
        if newWord is not "":
            result.append(newWord)
    for el in sorted(result):
            print(el)    

parser("this ! has lots of 432 numbers and @#$%@ symbols and we #@ need to remove them and sort alphabetically OK@@AY!")