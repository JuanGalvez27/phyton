# se usan las tuplas porque son inmutables
# son mucho más rápidas que las listas

x = (1,2,3)
print(x)
print(type(x))
# print(dir(x))

y = tuple((1,2,3,4)) # constructor

print(y)

z = (1)
print(z)
print(type(z))


z = (1,) # para especificar que es una tupla de un solo elemento hay que ponerle una coma despues del valor
print(z)
print(type(z))

# del z elimina la tupla 

print(z)

locations = {
  "Tokyo" : (45.12341234, 27.1234) # se guardan las coordenadas como una tupla ya que no cambiarán y son varios valores independientes
}