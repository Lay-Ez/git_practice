from random import randint

def factorial(n):
    result = 1
    while n != 0:
        result *= n
        n -= 1
    return result


#print(factorial(5))


def fibonacci(n):
    first_num = 1
    second_num = 1
    result = 0
    while n > 2:
        result = first_num + second_num
        first_num = second_num
        second_num = result
        n -= 1
    return result

#print(fibonacci(10))

def sum_digits(num):
    if num//10 == 0:
        return num
    else:
        return num%10 + sum_digits(num//10)

#print(sum_digits(123))

def find_min(lst):
    if len(lst) == 1:
        return lst[0]
    elif len(lst) == 0:
        return None
    else:
        if lst[0] > lst[-1]:
            return find_min(lst[1:])
        else:
            return find_min(lst[:-1])


#my_list = []
#print(find_min(my_list))

def is_palindrome(text):
    # takes in the string and returns True if string is
    # a palindrome
    if len(text) == 0:
        return True
    if len(text) <= 2:
        return text[0] == text[-1]
    else:
        return text[0] == text[-1] and is_palindrome(text[1:-1])

#print(is_palindrome("holaaloh"))

def depth_custom(tree):
    if not tree:
        return 0
    if tree["left_child"] == None and tree["right_child"] == None:
        return 1
    else:
        if tree["left_child"]:
            return 1 + depth(tree["left_child"])
        else:
            return 1 + depth(tree["right_child"])

def depth(tree):
    if not tree:
        return 0
    else:
        left_depth = depth(tree["left_child"])
        right_depth = depth(tree["right_child"])
        if left_depth > right_depth:
            return 1 + left_depth
        else:
            return 1 + right_depth

def depth_iter(tree):
    result = 0
    queue = [tree]
    while queue:
        level_count = len(queue)
        for i in range(0, level_count):
            child = queue.pop(0)
            if child["left_child"]:
                queue.append(child["left_child"])
            if child["right_child"]:
                queue.append(child["right_child"])
        result += 1
    return result


def build_bst(my_list):
  if len(my_list) == 0:
    return None

  mid_idx = len(my_list) // 2
  mid_val = my_list[mid_idx]

  tree_node = {"data": mid_val}
  tree_node["left_child"] = build_bst(my_list[ : mid_idx])
  tree_node["right_child"] = build_bst(my_list[mid_idx + 1 : ])

  return tree_node


# test cases
counter = 0
for i in range(1000):
    random_list = [randint(1, 101) for num in range(randint(1, 500))]
    tree_level = build_bst(sorted(random_list))
    if (depth(tree_level) != depth_custom(tree_level) or
         depth_iter(tree_level) != depth(tree_level) or
          depth_iter(tree_level) != depth_custom(tree_level)):
        counter += 1
print(counter)
