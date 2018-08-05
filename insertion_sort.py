#Erin Cox
import timeit

def insertionSort(inputList):
    for index in range(1, len(inputList)):
        currentVal = inputList[index]
        pos = index
        
        while pos > 0 and inputList[pos - 1] > currentVal:
            inputList[pos] = inputList[pos - 1]
            pos = pos - 1
            
        inputList[pos] = currentVal
        
    return inputList

inputList = [1,10,9,2,5,3,4,7,8,6]
sortedList = insertionSort(inputList)
print(sortedList)

t = timeit.Timer("insertionSort(inputList)", "from __main__ import insertionSort, inputList")
print("time taken: ", t.timeit(number=1))