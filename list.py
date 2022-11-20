demoList = [1,"rqwe",2.343, True, [4,63,3]]
colors = ["Blues" , "Green", "pink"]

#constructor
numberList = [ ]

numberList = list((1,2,3,4))
print(numberList)

# creat a list with the elements in the range
numberList2= list(range(0,10))
print(numberList2)

print(len(colors))
print(len(demoList[4]))
print("Green" in colors)

#colors.append(["violet", "yellow"]) # Agrega los elementos como uno solo, en este caso, una tupla
colors.extend(("gray", "red")) # Agrega los elementos independientes

colors.insert(1, "orange") # adds an element in an index
colors.insert(len(colors), "cyan") # insert an element in the end of the list

print(colors)

colors.pop() # delete the last element in the list
colors.remove("orange") # delete an specific value of the list
colors.pop(1) # remove the item in an index
colors.sort()

print(colors)
colors.sort(reverse=True)
print(colors)

print(colors.index("red"))
print(colors.count("red"))
print(colors)

colors.clear() # delete all the elements of the list

print(colors)