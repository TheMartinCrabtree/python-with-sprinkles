
mytuple1 = ("Simple String",)
mytuple2 = ("tuple2 string", 4)

mylist = ["first list string", 22, "last list string"]
mytuple3 = tuple(mylist)

mytuple4 = ("a", "p", "p", "l", "e")

print(mytuple1)
print(mytuple2)
print(mytuple3)
print(mytuple4.count("p"))
print(mytuple4.index("p"))
# convert to list
print(list(mytuple4))
