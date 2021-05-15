# lista
numberList = []
print(numberList)

numberList = [1, 2, 2, 4]
print(numberList)
print(len(numberList))

numberList.append(5)
print(numberList)

numberList[0] = 0
print(numberList)

for number in numberList:
    print(number)

fruitList = ["apple", "strawberry"]
for a in fruitList:
    print(a)

""" # ejercicio
numberList = range(1, 20)
# sacar la suma de todos los numeros
total = 0
for number in numberList:
    total += number
print(total) """

print(type(fruitList))


# tuplas
dataTuple = (1, "java", 1981)
print(type(dataTuple))

print(dataTuple[1])
id, language, year = dataTuple
print(id)
print(year)

for data in dataTuple:
    print(data)

dataList = list(dataTuple)
dataList.append("bal")
dataTuple = tuple(dataList)
id, language, year, developer = dataTuple

for data in dataTuple:
    print(data)


# ejercicio
dataTuple = (1, "dragonball", "japon", ("goku", "krilin"))
# id, serie, pais, personajes, listar los personajes
