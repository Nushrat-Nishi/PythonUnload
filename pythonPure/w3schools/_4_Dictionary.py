# A dictionary is a collection which is unordered, changeable and indexed. In Python dictionaries are written with curly brackets, and they have keys and values.

aDict = {"Sky" : "Blue",
         "Water" : "Transparent",
         "Soil" : "Ash"}

print(aDict)

aDict["Soil"] = "Black"
print("Change the Soil color to Black:", aDict)


# note that keywords are not string literals
# note the use of equals rather than colon for the assignment
bDict = dict(Sky = "Blue", Water = "Transparent", Soil = "Ash")
print("Using the dict() constructor to make a dictionary : ", bDict)

bDict["Laptop"] = "White"
print("Adding an item to the dictionary is done by using a new index key and assigning a value to it : ", bDict)

del(bDict["Soil"])
print("Removing a dictionary item must be done using the del() function in python : ", bDict)


print("The len() function returns the size of the dictionary : ", len(bDict))