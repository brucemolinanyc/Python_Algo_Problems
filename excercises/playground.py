# def numJewelsInStones(jewels, stones):
#     output = 0
#     for jewel in jewels:
#         for stone in stones:
#             if jewel == stone:
#                 output += 1
#     return output

def numJewelsInStones(J, S):
    output = 0 
    for jewel in J:
        output += S.count(jewel)
    return output

# print(numJewelsInStones('aA', 'aAAbbbb'))

def balancedStringSplit(str):
    l_count = 0
    r_count = 0
    total = 0
    for i in range(len(str)):
        if str[i] == "L":
            l_count += 1 
        if str[i] == "R":
            r_count += 1
        if l_count == r_count:
            total += 1
            l_count == 0, r_count == 0
    return total

 

# print(balancedStringSplit("LLLLRRRR"))
        
def removeOuterParen(string):
    result = []
    count = 0
    for i in string:
        if i == "(":
            count += 1 
        else:
            count -= 1
        if count == 1 and i == "(":
            pass
        elif count == 0 and i == ")":
            pass
        else:
            result.append(i)
    return "".join(result)


# print(removeOuterParen("(()())(())"))


# def numJewelsInStones(jewels,stones):
#     count = 0 
#     for i in jewels:
#         count += stones.count(i)
#     return count 

# print(numJewelsInStones("aA", "aAAbbbb"))

def balancedStringSplit(string):
    l_count = 0
    r_count = 0 
    total = 0 
    for i in range(0, len(string)):
        if string[i] == "L":
            l_count += 1
        if string[i] == "R":
            r_count += 1 
        if l_count == r_count:
            total += 1
            l_count = 0
            r_count = 0 
    return total

# print(balancedStringSplit('RLRRLLRLRL'))



class Person:
    def __init__(self, fname, lname):
        self.fname = fname
        self.lname = lname
    
    def printname(self):
        print(self.fname, self.lname)

class Student(Person):
    def __init__(self, fname, lname, year):
        super().__init__(fname, lname)
        self.year = year
    
    def welcome(self):
        print(f"welcome {self.fname} {self.lname} to the graduating class of {self.year}")

    def printname(self):
        print(f"i'm a student and my name is {self.fname}")

