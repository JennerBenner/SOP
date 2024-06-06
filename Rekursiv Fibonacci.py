def fibonacci_tal(n):
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci_tal(n - 1) + fibonacci_tal(n - 2)
print(fibonacci_tal(n))