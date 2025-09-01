k = 5
parts = []
for i in range(k):
    parts.append(str(2*i + 1))
    if i != k - 1:
        parts.append("*")
print(" ".join(parts[:1]))
print(" ".join(parts[:3]))
print(" ".join(parts[:5]))
print(" ".join(parts[:7]))
print(" ".join(parts[:9]))