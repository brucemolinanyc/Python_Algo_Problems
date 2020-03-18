#https://www.w3resource.com/python-exercises/

def twinkle():
    print("Twinkle, twinkle little star")
    print("     How I wonder what you are!")
    print("             Up above the world so high,")
    print("             Like a diamond in the sky")
    print("Twinkle, twinkle little star")
    print("     How I wonder what you are")

# print("Twinkle, twinkle, little star, \n\tHow I wonder what you are! \n\t\tUp above the world so high, \n\t\tLike a diamond in the sky. \nTwinkle, twinkle, little star, \n\tHow I wonder what you are!")

# twinkle()

# Write a Python program to get the Python version you are using.
def version():
    import sys
    print(f'we are using Python {sys.version}')

# version()

#Write a program to display the current date and time 
def datetime():
    import datetime
    now = datetime.datetime.now()
    print("Current date and time:")
    print(now.strftime("%Y-%m-%d %H:%M:%S"))

# datetime()

#Write a Python program which accepts the radius of a circle from the user and compute the area.
def circle_area(radius):
    print( round(( (radius**2) * 3.14),1) )

# circle_area(1.1)


#Write a Python program which accepts the user's first and last name and print them in reverse order with a space between them
def name_backwards():
    first = input("Please enter your first name: ")
    last = input("Please enter your last name: ")
    print(f'Your name backwards is {first[::-1]} {last[::-1]}')
    print(f'Your name reversed is {last} {first}')

# name_backwards()


#Write a Python program which accepts a sequence of comma-separated numbers from user and generate a list and a tuple with those numbers.
def number_format():
    values = input("enter some values: ")
    my_list = values.split(",")
    my_tuple = (values)

    print(f'List: {my_list}')
    print(f'Tuple {my_tuple}')


# number_format()

#Write a Python program to accept a filename from the user and print the extension of that.
def file_extension():
    file = input('enter your filename: ')
    while "." not in file:
        print("please enter a proper filename with a '.' extension")
        file = input("please enter a filename again: ")
    file_type = file.split(".")[-1]
    print(f'The extension of the file is {file_type}')

# file_extension()

#Write a Python program to display the first and last colors from the following list.
def first_last(list):
    print(f"the first item is {list[0]}")
    print(f"the last item is {list[-1]}")    

# first_last(['red', 'green', 'white', ' black'])

#Write a Python program to display the examination schedule. (extract the date from exam_st_date).
def date(tuple):
    if len(tuple) is not 3:
        print("please enter a tuple format with three items")
    else:
        print(f'The examination will start from: {tuple[0]}/{tuple[1]}/{tuple[2]} ')

# date((11,12,32,34))

#Write a Python program that accepts an integer (n) and computes the value of n+nn+nnn. 
def value_addition():
    num = input("give me a number x and I will compute x + x + xxx: ")
    while num.isdigit() is False:
        print("please enter a number only")
        num = input(" please enter a number x and I will compute x + x + xxx: ")
    num1 = num 
    num2 = num+num
    num3 = num+num+num
    result = int(num) + int(num2) + int(num3)
    print(f"The result of {num1} + {num2} + {num3} is {result}")

value_addition()