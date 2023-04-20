n = int(input())

a = []
for i in range (n):
    a.append(input())
b = list(set(a))
b.sort()
b.sort(key=len)
for i in b:
    print(i)