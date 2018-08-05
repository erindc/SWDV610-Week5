#Erin Cox
import timeit

def selectionSort(inputList):
    for swapNum in range(len(inputList)-1, 0, -1):
        maxPos = 0
        for pos in range(1, swapNum+1):
            if inputList[pos] > inputList[maxPos]:
                maxPos = pos
            inputList[swapNum], inputList[maxPos] = inputList[maxPos], inputList[swapNum]
    return inputList

inputList = [1,10,9,2,5,3,4,7,8,6]
sortedList = selectionSort(inputList)
print(sortedList)

t = timeit.Timer("selectionSort(inputList)", "from __main__ import selectionSort, inputList")
print("time taken: ", t.timeit(number=1))