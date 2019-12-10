

def countdown(x):
    while x <= 0:
        return
    else:
        countdown(x-1)

print(countdown(10))


def factorial(x):
    if x == 1:
        return 1
    else:
        return x * factorial(x-1)

print(factorial(3))

def until_twenty(x):
    if x == 20:
        return 0
    else: 
        return x + until_twenty(x + 1)

print(until_twenty(18))


def sum(arr):
    if list == []:
        return 0
    return list[0] + sum(list[1:])    

def count(arr):
    if list == []:
        return 0
    return list[0] + count(list[1:])