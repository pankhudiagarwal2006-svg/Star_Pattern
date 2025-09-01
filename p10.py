w = 10
left = 1
while left <= w // 2:
    if left == w // 2:
        print("*" * w)
    else:
        gap = w - 2*left
        print("*" * left + " " * gap + "*" * left)
    left += 1