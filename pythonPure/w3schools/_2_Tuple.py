# A tuple is a collection which is ordered and unchangeable. In Python tuples are written with round brackets.
aTuple = ("apple", "banana", "cherry")
print(aTuple)

print("Return the item in position 2 : ", aTuple[2])

bTuple = tuple(("apple", "banana", "cherry"))
print("Using the tuple() constructor to make a tuple : ", bTuple)

print("The len() method returns the number of items in a tuple : ", len(bTuple))