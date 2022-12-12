def fibonacci(n):
    if not n:
        return 0
    if n < 1:
        return 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)
