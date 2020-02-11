def writeFile():
    with open('myFile.txt', 'w') as open_file:
        open_file.write('this is my string')
        open_file.write('\n')
        open_file.write('this is my string')
        open_file.write('\n')    
        open_file.write('this is my string')
        open_file.write('\n')
        open_file.write('this is my string')


# if __name__ == "main":

writeFile()