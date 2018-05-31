print("Open the file demofile.txt and append content to the file : ")
f = open("demofile.txt", "a")
f.write("Add this line to the exsisting file!")

print("\nOpen the file demofile.txt and read the existing content : ")
f = open("demofile.txt", "r")
print(f.read())

print("\nOpen the file demofile.txt and overwrite any existing content : ")
f = open("demofile.txt", "w")
f.write("This line will overwrite any existing content.")

print("\nOpen the file demofile.txt and read the existing content : ")
f = open("demofile.txt", "r")
print(f.read())

print("\nTo create a new file in Python, use the open() method, with one of the following parameters : ")
# "x" - Create - will create a file, returns an error if the file exist.
#f = open("myfile1.txt", "x")

# "w" - Write - will create a file if the specified file does not exist. If the specified file exists, then no error.
f = open("myfile.txt", "w")

# "a" - Append - will create a file if the specified file does not exist. If the specified file exists, then no error.
f = open("myfile1.txt", "a")

print("\nTo delete a file, you must import the OS module, and run its os.remove() function : ")

import os
os.remove("myfile.txt")

print("\nCheck if the file exist before trying to delete it : ")
if os.path.exists("myfile.txt") :
    os.remove("myfile.txt")
else:
    print("The file doesn't exists.")


print("\nTo delete an entire folder, use the os.rmdir() method. You can only remove empty folders.")
os.rmdir("myfolder")