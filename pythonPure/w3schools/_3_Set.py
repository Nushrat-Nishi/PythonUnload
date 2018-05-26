# A set is a collection which is unordered and unindexed. In Python sets are written with curly brackets.

aSet = {"apple", "banana", "cherry"}
print(aSet)

bSet = set(("apple", "banana", "cherry"))
print("Using the set() constructor to make a set:", bSet)

bSet.add("Strawberry")
print("Using the add() method to add an item:", bSet)

bSet.remove("banana")
print("Using the remove() method to remove an item : ", bSet)

print("Using the len() method to return the number of items : ", len(bSet))