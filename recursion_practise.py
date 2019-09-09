from functools import lru_cache

@lru_cache(maxsize = 10000)
def fibonacci(n):
    if n == 1:
        return 1
    if n == 2:
        return 1
    if n > 2:
        return fibonacci(n-2) + fibonacci(n-1)
for i in range(2, 501):
    print(fibonacci(i)/fibonacci(i-1))
