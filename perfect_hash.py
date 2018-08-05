#Erin Cox

def hash(inputList, tableSize):
    hashVals = {}
    for index in range(len(inputList)):
        sum = 0
        for i in inputList[index]:
            sum += ord(i)^2
        hashVals[sum%tableSize] = inputList[index]

    return hashVals



inputList = ['bob', 'jo', 'suzy', 'sarah']
tableSize = 13
hashValues = hash(inputList, tableSize)
print(hashValues)