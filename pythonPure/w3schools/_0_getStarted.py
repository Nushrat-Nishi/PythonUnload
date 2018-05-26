print("Hello, World!")

if(5>2):{
    print("Five is greater than two!")
}

#Comment in Python
print("Hello, world!")

"""This is a 
multiline comment"""
print("Hello, world!")


#Python has no command for declaring a variable. A variable is created the moment you first assign a value to it.
x= 5
y = "Nishi"
print(x)
print(y)

#Variables change type after they have been set.
x = "Mahmood"
print("Variables change type after they have been set: "+ x) #To combine both text and a variable, Python uses the + character:

x = "Awesome"   # no semicolon needed!
y = "Python is "+x  #You can also use the combine the + character to add a variable to another variable.
print(y)

#For numbers, the + character works as a mathematical operator
x = 5
y = 10
print("+ character works as a mathematical operator: ",(x+y))


#Variables of numeric types are created when you assign a value to them
x = 1 # int
y = 2.8 # float
z = 1j # complex

print("Type of x : ", type(x))
print("Type of y : ", type(y))
print("Type of z : ", type(z))


x = int(1)
y = int(2.8)
z = int("3")
print(x)
print("Type of x after casting : ", type(x))
print(y)
print("Type of y after casting : ", type(y))
print(z)
print("Type of z after casting : ", type(z))



