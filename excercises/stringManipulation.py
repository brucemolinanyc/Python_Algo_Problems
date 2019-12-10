# find method - returns index based on what you searched for
message = "hello world"

index = message.find("world")
print(message[index:])


for i in message.split(" "):
    print(i)

#slice method - grab a piece of the message using substrings
print(message[0:5])

#count number of items in a string
totals = {}
for i in message:
    if i in totals:
        totals[i] += 1 
    else:
        totals[i] = 1
print(totals)



print("keys", totals.keys())
print("values", totals.values())
print(list(totals))
print(list(totals.keys()))
print(list(totals.values()))

# for i in range(len(list(totals))):
#     print(f"the total amount of {list(totals.keys())[i]} is {list(totals.values())[i]} ")

for i in set(message):
    print(f"the count of letter {i} is {message.count(i)}")

 
 
#find unique letters or integers
for el in message:
    if message.count(el) > 1:
        next
    else:
        print(f"{el} only appears once in the string")


