from random import randrange
from random import randint

def quicksort(list, start, end):
    if start >= end:
        return

    pivot_idx = randrange(start, end+1)
    pivot_element = list[pivot_idx]

    list[pivot_idx], list[end] = list[end], list[pivot_idx]

    lesser_pointer = start
    for i in range(start, end):
        if list[i] < pivot_element:
            list[i], list[lesser_pointer] = list[lesser_pointer], list[i]
            lesser_pointer += 1
    list[lesser_pointer], list[end] = list[end], list[lesser_pointer]

    quicksort(list, start, lesser_pointer - 1)
    quicksort(list, lesser_pointer + 1, end)
