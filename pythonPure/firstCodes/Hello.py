import random
print ("Hello, Python!");

x=0;
y=1;

if (x==0):
    print ("x is True");
    print ("True");
elif(x==y):
    print ("False");

counter = 100          # An integer assignment
miles   = 1000.0       # A floating point
name    = "John"       # A string

print (counter);
print (miles);
print (name);

foo = ['a', 'b', 'c', 'd', 'e']
from random import randrange
random_index = randrange(0,len(foo))
print ("------- : ",foo[random_index])