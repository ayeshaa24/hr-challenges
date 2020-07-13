# BASECASES:
# fibonacci(0) = 0
# fibonacci(1) = 1
# STEPCASE:
# fibonacci(n) = fibonacci(n-1) + fibonacci(n-2)

def fibonacci(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n-1) + fibonacci(n-2)


n = int(input())
print(fibonacci(n))
