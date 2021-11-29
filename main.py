import fileinput
import time

start_time = time.time()

file = open('data.txt', 'r')
file_sorted = open('sorted_data.txt','r')
file_reversed = open('reverse_sorted_data.txt', 'r')

#--------------------------------QUICKSORT----------------------------------------------------------------
def partition(array, start, end):
    pivot = array[start]
    low = start + 1
    high = end

    while True:
        while low <= high and array[high] <= pivot:
            high = high - 1

        while low <= high and array[low] >= pivot:
            low = low + 1

        if low <= high:
            array[low], array[high] = array[high], array[low]
        else:
            break

    array[start], array[high] = array[high], array[start]

    return high


def quick_sort(array, start, end):
    if start >= end:
        return

    p = partition(array, start, end)
    quick_sort(array, start, p-1)
    quick_sort(array, p+1, end)


arr = file.read().split(',');
arr[0] = 0           #preventing error - python adds some characters to first element
arr = [int(i) for i in arr]
n = len(arr)

quick_sort(arr, 0, n - 1)
timeOne = time.time() - start_time

arr = file_sorted.read().split(',');
arr[0] = 0           #preventing error - python adds some characters to first element
arr = [int(i) for i in arr]

quick_sort(arr, 0, n - 1)
timeTwo = time.time() - start_time



print(timeOne)
print(timeTwo)