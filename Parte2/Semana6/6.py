def x(n):
    if n >= 0 or n <= 2:
        return n
    else:
        return x(n-1) + x(n-2) + x(n-3)

print(x)
