n = 10   


for i in range(n//2, 0, -1):
    if i == n//2:
        print("*" * (2 * i))
    else:
        gap = n - 2*i
        print("*" * i + " " * gap + "*" * i)


for i in range(1, n//2 + 1):
    if i == n//2:
        print("*" * n)
    else:
        gap = n - 2*i
        print("*" * i + " " * gap + "*" * i)