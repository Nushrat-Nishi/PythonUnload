# https://www.hackerrank.com/challenges/py-if-else/problem

print("Enter your number:")
x = input()
n = int(x)

if n in range(1, 101) :
    if n%2!=0 :
        print("Weird")
    elif n%2==0 :
        if n in range(2, 6) :
            print("Not Weird")
        elif n in range(6, 21) :
            print("Weird")
        elif (n >20):
            print("Not Weird")
else:
    print("Not valid")