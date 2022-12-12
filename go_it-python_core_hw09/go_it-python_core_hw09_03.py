def caching_fibonacci():
    CACHE = {0: 0,
             1: 1
             }

    def fibonacci(n):
        if n in CACHE:
            return CACHE[n]
        else:
            CACHE[n] = fibonacci(n - 1) + fibonacci(n - 2)
            return CACHE[n]

    return fibonacci


# new_fib = caching_fibonacci()
# print(new_fib(11))
# print(new_fib(11))
# print(new_fib(12))
