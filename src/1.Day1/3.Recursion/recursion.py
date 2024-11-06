# Factorial using recursion

def factorial(n):
    if n == 0:
        return 1
    return n * factorial(n - 1)

n = 5
print(f'Factorial of {n}: {factorial(n)}')

# Fibonacci series using recursion
def fibonacci(n):
    if n <= 1:
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)

n = 10
print(f'Fibonacci series of {n}: {fibonacci(n)}')