aList = ["Cherry", "Apple", "Banana", "Apple"]
print("A list is ordered and changeable. Allows duplicate members : ", aList)
aList[1] = "Orange"
print("List is changeable : ", aList)


bList = list(("Cherry", "Apple", "Banana", "Apple")) # note the double round-brackets
print("Using the list() constructor to make a list : ", bList)

bList.append("Strawberry")
print("Using the append() method to append an item : ", bList)

bList.remove("Banana")
print("Using the remove() method to remove an item : ", bList)

print("The len() method returns the number of items in a list : ", len(bList))