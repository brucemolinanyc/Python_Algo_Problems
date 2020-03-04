# def grabWords(str):
#     result = []
#     for word in str.split(" "):
#         newStr = ""
#         for char in word:
#             if char.isalpha():
#                 newStr += char
#         if newStr is not "":
#             result.append(newStr) 
#     for word in sorted(result):
#         print(word)




# print(grabWords("this str!ing #@ has symbols @# a%t fir$st but we parsed them!!"))

def interest_calculator(deposit, annual_interest_rate, contributions, number_of_years ):
    final_value = deposit 
    years = number_of_years
    interest = annual_interest_rate/100 

    while number_of_years >= 1:
        final_value = final_value + contributions + ((final_value + contributions) * interest)
        number_of_years -= 1

    print("Your deposit of {} compounded over {} years is equal to ${} dollars".format(deposit, years, final_value))
    print("The interest gained over {} years is ${} dollars".format(years, round((final_value - (contributions * years) - deposit), 2)))

    

# interest_calculator(100, 10, 50, 3)

"""
100 + 50 + 15 = 165
165 + 50 + 21.5 = 236.5
236.5 + 50 + 28.65 = 315.15
"""
65.15


# def solution(arr):
#     a = set(arr)
#     ans = 1
#     while ans in a:
#        ans += 1
#     return ans

# print(solution([1,2,3,4]))
def numberOfSteps (num):
    steps = 0
    while num >= 1:
        steps += 1 
        if num % 2 == 0:
            num = num/2
        else:
            num = num -1 
    return steps
        
print(numberOfSteps(14))