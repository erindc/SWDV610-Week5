#Erin Cox
import timeit

def bubbleSort(inputList):
    for swapNum in range(len(inputList)-1, 0, -1):
        for i in range(swapNum):
            if inputList[i] > inputList[i+1]:
                inputList[i], inputList[i+1] = inputList[i+1], inputList[i]
    return inputList

inputList = [1,10,9,2,5,3,4,7,8,6]
sortedList = bubbleSort(inputList)
print(sortedList)

t = timeit.Timer("bubbleSort(inputList)", "from __main__ import bubbleSort, inputList")
print("time taken: ", t.timeit(number=1))