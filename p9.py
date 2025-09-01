w = 10                 
left = w // 2
right = w // 2
for i in range(left, 0, -1):
    if i == left:
        print("*" * (2 * i))
    else:
        gap = (w - 2*i)
        print("*" * i + " " * gap + "*" * i)