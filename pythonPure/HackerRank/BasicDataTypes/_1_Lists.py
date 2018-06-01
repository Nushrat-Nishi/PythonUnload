# https://www.hackerrank.com/challenges/python-lists/problem

N = int(input())

aList = []

for x in range(N):
    line = input()

    lines = line.split(" ")

    if lines[0] == "insert":
        aList.insert(int(lines[1]), int(lines[2]))

    elif lines[0] == "print" :
        print(aList)

    elif lines[0] == "remove" :
        aList.remove(int(lines[1]))

    elif lines[0] == "append":
        aList.append(int(lines[1]))

    elif lines[0] == "sort":
        aList.sort(key=int)

    elif lines[0] == "pop":
        aList.pop()

    elif lines[0] == "reverse":
        aList.reverse()