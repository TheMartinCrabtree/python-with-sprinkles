# list (array)

mylist = ["list item 1", "list item 2", "list item 3"]
print("Current list is: ")
print(mylist)

print("-1 position is: ")
print(mylist[-1])

print("len(mylist)) is: ")
print(len(mylist))

for i in mylist:
    print("Position " + i + " is: ")
    print(i)

print("Is list item 1 in the list?")
if "list item 1" in mylist:
    print("yes")
else: 
    print("no")

# mylist.insert(index, var)  mylist.pop()  mylist.remove(var) mylist.clear() mylist.reverse()
# mylist.sort() is destructive   sorted(mylist) returns a new sorted list
# mylist = [var] * int
# mylist = [intStart : intEnd ]
# mylist = [intStart :: intStep] return a new list with only the intStep intervals (ie. every other for 2)
# newlist = mylist.copy() or copy(mylist) or mylist[:]
# newlist = [i*i for i in mylist]  create a new list with the squared values of each list item in mylist