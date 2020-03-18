# # def grabWords(str):
# #     result = []
# #     for word in str.split(" "):
# #         newStr = ""
# #         for char in word:
# #             if char.isalpha():
# #                 newStr += char
# #         if newStr is not "":
# #             result.append(newStr) 
# #     for word in sorted(result):
# #         print(word)




# # print(grabWords("this str!ing #@ has symbols @# a%t fir$st but we parsed them!!"))

# def interest_calculator(deposit, annual_interest_rate, contributions, number_of_years ):
#     final_value = deposit 
#     years = number_of_years
#     interest = annual_interest_rate/100 

#     while number_of_years >= 1:
#         final_value = final_value + contributions + ((final_value + contributions) * interest)
#         number_of_years -= 1

#     print("Your deposit of {} compounded over {} years is equal to ${} dollars".format(deposit, years, final_value))
#     print("The interest gained over {} years is ${} dollars".format(years, round((final_value - (contributions * years) - deposit), 2)))

    

# # interest_calculator(100, 10, 50, 3)

# """
# 100 + 50 + 15 = 165
# 165 + 50 + 21.5 = 236.5
# 236.5 + 50 + 28.65 = 315.15
# """
# 65.15


# # def solution(arr):
# #     a = set(arr)
# #     ans = 1
# #     while ans in a:
# #        ans += 1
# #     return ans

# # print(solution([1,2,3,4]))
# def numberOfSteps (num):
#     steps = 0
#     while num >= 1:
#         steps += 1 
#         if num % 2 == 0:
#             num = num/2
#         else:
#             num = num -1 
#     return steps
        
# # print(numberOfSteps(14))

# # def smallerNumbersThanCurrent(arr):
# #     result = []
# #     for i in range(len(arr)):
# #         count = 0 
# #         for j in range(i+1, len(arr)):
# #             if arr[i] > arr[j]:
# #                 count += 1
# #         result.append(count)
# #     return result

# # print(smallerNumbersThanCurrent([8,1,2,2,3]))

        
# def test(a,b):
#     str_a = str(a)
#     str_b = str(b)
#     start_index = 0

#     while str_b != "":
#         temp_a = str_a
#         temp_b = str_b
#         while temp_a != "":
#             if temp_a[0] == temp_b[0]:
#                 temp_a = temp_a[1:] 
#                 temp_b = temp_b[1:]
#             else:
#                 break
#         if temp_a == "":
#             return start_index
#         str_b = str_b[1:]
#         start_index += 1
#     return -1 



# # print(test(44,143144523))



# def testb(a,b):
#     integers = 0
#     x = 1
#     while (x * (x + 1)) <= b:
#         if (x * (x+1)) >= a:
#             integers += 1
#         x = x + 1 
#     return integers

# print(testb(21,29))


# def find_colors(A, num, row, column):
#     if row >= len(A) or column >= len(A[row]):
#         return
#     A[row][column] = None 
#     if row+1 < len(A) and num ==A[row+1][column]:
#         find_colors(A, num, row+1, column)
#     if row-1 >= 0 and num == A[row-1][column]:
#         find_colors(A, num, row, column-1)
#     if column -1 >= 0 and num ==A[row][column-1]:
#         find_colors(A, num, row, column-1)
#     if column +1 <len(A[row]) and num ==A[row][column+1]:
#         find_colors(A, num, row, column +1)
    



# def solution(A):
#     # write your code in Python 3.6
#     num_colors = 0 
#     for i in range(len(A)):
#         for j in range(len(A[i])):
#             if A[i][j] != None:
#                 num = A[i][j]
#                 find_colors(A, num, i,j)
#                 num_colors +=1  
#     return num_colors


