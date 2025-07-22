#!/usr/bin/env python3
a = [10, 20, 30, 40, 50, 60]
b = [11, 12]

c = []
n=3
nnn = 3
print(f'n: {n}')
c = a[:n]
for i in range(len(b)):
    c.append(b[i])
for aa in a[n:]:
    c.append(aa)

print(a)
print(b)
print(c)
