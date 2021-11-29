#Bubblesort----------------------------------------------
import time

start_time = time.time()

file = open('data.txt', 'r')
file_sorted = open('sorted_data.txt','r')
file_reversed = open('reverse_sorted_data.txt', 'r')

def bubbleSort(arr):
    n = len(arr)

    # Traverse through all array elements
    for i in range(n):

        # Last i elements are already in place
        for j in range(0, n - i - 1):

            # traverse the array from 0 to n-i-1
            # Swap if the element found is greater
            # than the next element
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]

arr = file.read().split(',');
arr[0] = 0           #preventing error - python adds some characters to first element
arr = [int(i) for i in arr]

bubbleSort(arr)
timeOne = time.time() - start_time

arr = file_sorted.read().split(',');
arr[0] = 0           #preventing error - python adds some characters to first element
arr = [int(i) for i in arr]

bubbleSort(arr)
timeTwo = time.time() - start_time

arr = file_reversed.read().split(',');
arr[0] = 0           #preventing error - python adds some characters to first element
arr = [int(i) for i in arr]

bubbleSort(arr)
timeThree = time.time() - start_time

print(timeOne)
print(timeTwo)
print(timeThree)