#bubble sort algorithm
from random import randint

def swap(arr, index_1, index_2):
    temp = arr[index_1]
    arr[index_1] = arr[index_2]
    arr[index_2] = temp


def bubble_sort_minmax(arr):
    for i in arr:
        for i in range(len(arr)-1):
            if arr[i] > arr[i+1]:
                swap(arr, i, i+1)
    return arr

def bubble_sort_opt(arr):
    for i in range(len(arr)):
        for idx in range(len(arr)-i-1):
            if arr[idx] > arr[idx+1]:
                arr[idx], arr[idx+1] = arr[idx+1], arr[idx]
    return arr





nums = [randint(1, 10000) for num in range(1, 10001)]

#print(bubble_sort_minmax(nums))
#print(bubble_sort_opt(nums))
