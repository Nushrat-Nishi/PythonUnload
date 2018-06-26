# https://www.hackerrank.com/challenges/find-second-maximum-number-in-a-list/problem

if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split())

    inputList = list(arr)

    maxNumber = max(inputList)
    inputList.remove(maxNumber)

    while max(inputList)==maxNumber:
        inputList.remove(maxNumber)

    runnerUpScore = max(inputList)
    print(runnerUpScore)