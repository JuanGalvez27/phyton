myStr = "Hello World"

# print(dir(myStr))

print(myStr.upper()) # to upper case
print(myStr.lower()) # to lower case 
print(myStr.swapcase())  # swaps the case
print(myStr.capitalize()) # first character to upper case

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