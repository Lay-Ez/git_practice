def sparse_search(data, search_val):
    print("Data: {}".format(data))
    print("Search value: {}".format(search_val))
    first, last = 0, (len(data)) - 1

    while first <= last:
        mid = (first + last) // 2
        if not data[mid]:
            left, right = mid - 1, mid + 1
            while True:
                if left < first and right > last:
                    print("{} not found in the list".format(search_val))
                    return
                elif right <= last and data[right]:
                    mid = right
                    break
                elif left >= first and data[left]:
                    mid = left
                    break
                right += 1
                left -= 1

        if data[mid] == search_val:
            print("{} found at position {}".format(search_val, mid))
            return
        elif search_val < data[mid]:
            last = mid -1
        elif search_val > data[mid]:
            first = mid + 1
    print("{} not in the dataset".format(search_val))




sparse_search(["B", "", "C", "V", "A", "G", "", "", "", "D", "", "Z", "", "", "C"], "Z")
