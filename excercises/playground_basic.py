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

