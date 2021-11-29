#Mergesort--------------------------------------------------------------------------------------------

import time

start_time = time.time()

file = open('data.txt', 'r')
file_sorted = open('sorted_data.txt','r')
file_reversed = open('reverse_sorted_data.txt', 'r')

def mergeSort(myList):
    if len(myList) > 1:
        mid = len(myList) // 2
        left = myList[:mid]
        right = myList[mid:]

        mergeSort(left)
        mergeSort(right)

        i = 0
        j = 0
        k = 0

        while i < len(left) and j < len(right):
            if left[i] <= right[j]:
                myList[k] = left[i]
                i += 1
            else:
                myList[k] = right[j]
                j += 1
            k += 1

        while i < len(left):
            myList[k] = left[i]
            i += 1
            k += 1

        while j < len(right):
            myList[k] = right[j]
            j += 1
            k += 1


arr = file.read().split(',');
arr[0] = 0           #preventing error - python adds some characters to first element
arr = [int(i) for i in arr]

mergeSort(arr)
timeOne = time.time() - start_time

arr = file_sorted.read().split(',');
arr[0] = 0           #preventing error - python adds some characters to first element
arr = [int(i) for i in arr]

mergeSort(arr)
timeTwo = time.time() - start_time

arr = file_reversed.read().split(',');
arr[0] = 0           #preventing error - python adds some characters to first element
arr = [int(i) for i in arr]

mergeSort(arr)
timeThree = time.time() - start_time

print(timeOne)
print(timeTwo)
print(timeThree)