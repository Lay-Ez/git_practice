from random import randint

def merge_sort(arr):
    if len(arr) <= 1:
        return arr
    middle_idx = len(arr)//2
    left_split = arr[:middle_idx]
    right_split = arr[middle_idx:]

    left_sorted = merge_sort(left_split)
    right_sorted = merge_sort(right_split)

    return merge(left_sorted, right_sorted)



def merge(left, right):
    result = []
    while left and right:
        if left[0] <= right[0]:
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

my_list = [randint(1, 100000) for i in range(100001)]

print(merge_sort(my_list))
