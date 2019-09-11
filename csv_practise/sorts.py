import random


def bubble_sort(arr, comparison_function):
  swaps = 0
  sorted = False
  while not sorted:
    sorted = True
    for idx in range(len(arr) - 1):
      if comparison_function(arr[idx], arr[idx + 1]):
        sorted = False
        arr[idx], arr[idx + 1] = arr[idx + 1], arr[idx]
        swaps += 1
  print("Bubble sort: There were {0} swaps".format(swaps))
  return arr

def quicksort(list, start, end, comparison_function):
  if start >= end:
    return
  pivot_idx = random.randrange(start, end + 1)
  pivot_element = list[pivot_idx]
  list[end], list[pivot_idx] = list[pivot_idx], list[end]
  less_than_pointer = start
  for i in range(start, end):
    if comparison_function(pivot_element, list[i]):
      list[i], list[less_than_pointer] = list[less_than_pointer], list[i]
      less_than_pointer += 1
  list[end], list[less_than_pointer] = list[less_than_pointer], list[end]
  quicksort(list, start, less_than_pointer - 1, comparison_function)
  quicksort(list, less_than_pointer + 1, end, comparison_function)


def merge_sort(arr, comparison_function):
    if len(arr) <= 1:
        return arr
    middle_idx = len(arr)//2
    left_split = arr[:middle_idx]
    right_split = arr[middle_idx:]

    left_sorted = merge_sort(left_split, comparison_function)
    right_sorted = merge_sort(right_split, comparison_function)

    return merge(left_sorted, right_sorted, comparison_function)



def merge(left, right, comparison_function):
    result = []
    while left and right:
        if not comparison_function(left[0], right[0]):
            result.append(left[0])
            left.pop(0)
        else:
            result.append(right[0])
            right.pop(0)

    if left:
        result += left
    if right:
        result += right
    return result
