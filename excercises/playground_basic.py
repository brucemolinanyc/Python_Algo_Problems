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


