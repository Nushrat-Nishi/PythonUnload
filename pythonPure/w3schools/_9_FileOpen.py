# Python has several functions for creating, reading, updating, and deleteing files.
# The key function for working with files in Python is the open() function.
# The open() function takes two parameters; filename, and mode.

# There are four different methods (modes) for opening a file:
# "r" - Read - Default value. Opens a file for reading, error if the file does not exist
# "a" - Append - Opens a file for appending, creates the file if it does not exist
# "w" - Write - Opens a file for writing, creates the file if it does not exist
# "x" - Create - Creates the specified file, returns an error if the file exist

# In addition you can specify if the file should be handled as binary or text mode
# "t" - Text - Default value. Text mode
# "b" - Binary - Binary mode (e.g. images)

# The open() function returns a file object, which has a read() method for reading the content of the file:

#f = open("demofile.txt")
# f = open("demofile.txt", "rt")


print("------------------------------------")
f = open("demofile.txt", "r")
print("By default the read() method returns the whole text : ", f.read())
print("------------------------------------")
f = open("demofile.txt", "r")
print("Specify how many character to return : ", f.read(5))
print("------------------------------------")
f = open("demofile.txt", "r")
print("Returning one line by using the readline() method : ", f.readline())
print("Returning 2nd line by using the readline() method : ", f.readline())
print("Returning 3rd line by using the readline() method : ", f.readline())