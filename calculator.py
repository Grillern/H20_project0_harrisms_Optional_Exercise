
def add(x, y):
    return x + y

def factorial(n):
    factorial = 1
    for i in range(1, int(n)+1):
        factorial *= i
    return factorial

def sin(x, N):
    taylor_sin = 0
    for n in range(N):
        taylor_sin += ((-1)**n) * (x**(2*n+1)) / factorial(2*n+1)
    return taylor_sin

def divide(x, y):
    return x/y

def cos(x, N):
    taylor_cos = 0
    for n in range(N):
        taylor_cos += ((-1)**n) * (x**(2*n)) / factorial(2*n)
    return taylor_cos

def power(x, y):
    return x ** y