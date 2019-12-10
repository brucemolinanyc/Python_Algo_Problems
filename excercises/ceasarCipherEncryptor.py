# def caesarCipherEncryptor(string, key):
#     alphaHashKeys = alphabet_as_keys()
#     alphaHashNumbers = alphabet_as_values()
#     newString = ""
#     for el in string:
#         newNumber = None
#         number = alphaHashKeys[el]
#         if number + key > 26:
#             newNumber = numberCompactor(number, key)
#             newString += alphaHashNumbers[newNumber]
#         else:
#             newString += alphaHashNumbers[number + key]
#     return newString
        

# def alphabet_as_values():
#     i = 97 #a in ascii 
#     j = 1
#     alpha = {}
#     while i < 123:
#         alpha[j] = chr(i)
#         j += 1 
#         i+= 1
#     return alpha  

# def alphabet_as_keys():
#     i = 97 #a in ascii 
#     j = 1
#     alpha = {}
#     while i < 123:
#         alpha[chr(i)] = j
#         j += 1 
#         i+= 1
#     return alpha 

# def numberCompactor(num, value):
#     while num + value > 26:
#         value -= 26
#     return num + value 



def caesarCipherEncryptor(string, key):
    newLetters = []
    newKey = key % 26 # the remainder basically the wrap around after z
    for letter in string: 
        newLetters.append(getNewLetter(letter, newKey))
    return "".join(newLetters)

def getNewLetter(letter, key):
    newLetterCode = ord(letter) + key 
    return chr(newLetterCode) if newLetterCode <= 122 else chr(96 + newLetterCode % 122) # remainder to account for wrapping around the Z

print(caesarCipherEncryptor("xyz", 2))
