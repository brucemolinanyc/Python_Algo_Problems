def getNthFib(n):
    fiboNums = [0,1] 
    while n > len(fiboNums):
        fiboNums.append(fiboNums[-1] + fiboNums[-2])
    return fiboNums[-1]


print(getNthFib(7))
    
