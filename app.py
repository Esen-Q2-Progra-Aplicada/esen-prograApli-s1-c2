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
dataTuple = (1, "dragonball", "japon", ["goku", "krilin"])
# id, serie, pais, personajes, listar los personajes

id, serie, pais, personajes = dataTuple
print(id)
print(serie)
print(pais)
print("personajes-->")
print(type(personajes))
for personaje in personajes:
    print("-", personaje)


# set
dataSet = {1, 2, 3, 2, 5, 6, 6, 7}
print(dataSet)

print(1 in dataSet)
print(9 in dataSet)

for data in dataSet:
    print(data)

dataSet.add(10)
print(dataSet)


# diccionario

dataDict = {"id": 1, "name": "bal", "age": 23}
print(dataDict["id"])
print(dataDict.keys())

for key in dataDict.keys():
    print(dataDict[key])

for value in dataDict.values():
    print(value)

dataDict["name"] = "balx"
print(dataDict)

for key, value in dataDict.items():
    print(key, value)
