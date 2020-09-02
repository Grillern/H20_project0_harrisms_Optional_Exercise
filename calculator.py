
def add(x, y):
    return x + y

def factorial(n):
    if type(n) is int and n >= 0:
        factorial = 1
        for i in range(1, int(n)+1):
            factorial *= i
        return factorial
    else:
        raise Exception(f"Factorial cannot be {type(n)} or a negative number. Type a natural number")
        
def sin(x, N):
    if type(x) is int:
        taylor_sin = 0
        for n in range(N):
            taylor_sin += ((-1)**n) * (x**(2*n+1)) / factorial(2*n+1)
        return taylor_sin
    else:
        raise Exception(f"Sin cannot be {type(x)}. Type an integer")

def divide(x, y):
    if type(x) and type(y) is int or float:
        return x/y
    else:
        raise Exception(f"Divide cannot be {type(x)} and {type(y)}. Type an integer or float")

def cos(x, N):
    if type(x) is int:
        taylor_cos = 0
        for n in range(N):
            taylor_cos += ((-1)**n) * (x**(2*n)) / factorial(2*n)
        return taylor_cos
    else:
        raise Exception(f"Cos cannot be {type(x)}. Type an integer")

def power(x, y):
    if type(x) and type(y) is int or float:
        return x ** y
    else:
        raise Exception(f"Power of cannot be {type(x)} and {type(y)}. Type an integer or float")
