# In Python a function is defined using the def keyword:

def printWelcomeMessage():
    print("Hello, world!")

printWelcomeMessage()
print("------------------------------------")
def printName(name):
    print("Hello, "+name)

printName("Nishi")
printName("Mahmood")
printName("Nushrat")

print("------------------------------------")
# Default Parameter Value
def findCountryName(country = "Netherlands"):
    printName("Country is : "+country)

findCountryName("Bangladesh")
findCountryName()


print("------------------------------------")
# Default Parameter Value
def testReturnValues(x):
    return x*20

print("Return value is : ",testReturnValues(5))

print("---------------***---------------------")
# The keyword lambda is used to create anonymous functions. These are essentially functions with no pre-defined name. They are good for constructing adaptable functions, and thus good for event handling.
testLambdaFunc = lambda i: i*2
print("Calling Lambda function : ", testLambdaFunc(3))
print("---------------***---------------------")
# Lambda defined functions can have more than one defined input, as shown here:
testLambdaFunc2 = lambda x,y : x*y
print("Lambda function with more than one input : ", testLambdaFunc2(4,7))

print("----------------***--------------------")
# The power of lambda is better shown when you generate anonymous functions at run-time.
def myfunc(n):
  return lambda i: i*n

doubler = myfunc(2)
tripler = myfunc(3)
val = 11
print("Doubled: " + str(doubler(val)) + ". Tripled: " + str(tripler(val)))
