import random

array = []

for i in range(0, 10):
    array.append(random.randrange(0,100))

print("Array to sort " + str(array))

def bubbleSort():
    for i in range(0,len(array)):
        for j in range(0,len(array)-i-1):
            if array[j] > array[j+1]:
                temp  = array[j+1]
                array[j+1] = array[j]
                array[j] = temp

bubbleSort()
print("Sorted array: " + str(array))
