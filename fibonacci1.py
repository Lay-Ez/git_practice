fibs = {}

def fibonacci(num):
    if num == 1:
        return 1
    if num == 2:
        return 1
    else:
        return fibonacci(num-2) + fibonacci(num-1)


for i in range(1, 100):
    print("{} : {}".format(i, fibonacci(i)))
