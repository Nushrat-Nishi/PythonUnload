a = "Nishi"
print(a[1])

b = "Mahmood"
print("From position 2 to 4 : ",b[2:5])


a = " Hello, Nishi! "
print("The strip() method removes any whitespace from the beginning or the end:", a.strip())

print("The len() method returns the length of a string: ", len(a))

print("The lower() method returns the string in lower case: ", a.lower())

print("The upper() method returns the string in upper case: ", a.upper())

print("The replace() method replaces a string with another string: ", a.replace("H", "M"))

print("The split() method splits the string into substrings if it finds instances of the separator: ", a.split(","))


# By using the input() method, the program prints the name to the screen:
print("Enter your name:")
x = input()
print("Hello, "+x)

#Python Identity Operators
x = ["apple", "banana"]
y = ["apple", "banana"]
z = x

print("z is the same object as x : ",x is z)
print("x is not the same object as y, even if they have the same content : ", x is y)
print("x is equal to y : ", x == z)


x = ["apple", "banana"]
print("A sequence with the value banana is in the list : ","banana" in x)
print("A sequence with the value pineapple is not in the list : ","pineapple" not in x)