myStr = "Hello World"

# print(dir(myStr))

print(myStr.upper())
print(myStr.lower())
print(myStr.swapcase()) 
print(myStr.capitalize())

print(myStr.replace("Hello", "Bye").upper())
print(myStr.count("l"))

print(myStr.startswith("Hello"))
print(myStr.endswith("ld"))
print(myStr.split())
print(myStr.find("l"))
print(len(myStr))

print(myStr[6])

myName = "Juan"
print(f"My name is {myName}") #Like template literals
print("My name is {0}".format(myName))