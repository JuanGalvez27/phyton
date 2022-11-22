def hello(a="pepito"):  #def: definition of a function. por defecto usa pepito
  print("hello " + a)

hello("Juan")
hello()

#lambf

add = lambda number1, number2: number1 + number2
print(add(10,30))