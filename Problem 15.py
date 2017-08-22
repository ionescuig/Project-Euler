n = 20
paths = 1

for i in range(n):
    paths *= 2*n - i
    paths /= i+1

print(paths)
