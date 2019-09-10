from random import randint

def radix_sort(to_sort):
    max_element = max(to_sort)
    max_exponent = len(str(max_element))
    being_sorted = to_sort[:]

    for exponent in range(max_exponent):
        pointer = exponent + 1
        index = -pointer
        digits = [[] for i in range(10)]

        for number in being_sorted:
            number_str = str(number)
            try:
                digit = number_str[index]
                digit = int(digit)
            except IndexError:
                digit = 0
            digits[digit].append(number)

        being_sorted = []
        for numeral in digits:
            being_sorted.extend(numeral)
    return being_sorted

my_list = [randint(1,1000000) for i in range(1000001)]
print(radix_sort(my_list))
