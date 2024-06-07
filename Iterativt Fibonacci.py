def fibonacci_tal(n):
    a, b = 1, 0
    for i in range(n):
        a, b = b, a + b
    return b
print(fibonacci_tal(n))

