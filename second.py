#Heapsort-------------------------------------------------------------------------------------------
import time

start_time = time.time()

file = open('data.txt', 'r')
file_sorted = open('sorted_data.txt','r')
file_reversed = open('reverse_sorted_data.txt', 'r')

def heapsort(MyList):
    n = len(MyList)
    for i in range(n // 2, -1, -1):
        heapify(MyList, n - 1, i)

    for i in range(n - 1, -1, -1):
        MyList[i], MyList[0] = MyList[0], MyList[i]

        heapify(MyList, i - 1, 0)

def heapify(MyList, n, i):
    max, left, right = i, 2 * i + 1, 2 * i + 2

    if left <= n and MyList[left] > MyList[max]:
        max = left

    if right <= n and MyList[right] > MyList[max]:
        max = right

    if max != i:
        MyList[i], MyList[max] = MyList[max], MyList[i]
        heapify(MyList, n, max)


arr = file.read().split(',');
arr[0] = 0           #preventing error - python adds some characters to first element
arr = [int(i) for i in arr]

heapsort(arr)
timeOne = time.time() - start_time

arr = file_sorted.read().split(',');
arr[0] = 0           #preventing error - python adds some characters to first element
arr = [int(i) for i in arr]

heapsort(arr)
timeTwo = time.time() - start_time

arr = file_reversed.read().split(',');
arr[0] = 0           #preventing error - python adds some characters to first element
arr = [int(i) for i in arr]

heapsort(arr)
timeThree = time.time() - start_time

print(timeOne)
print(timeTwo)
print(timeThree)