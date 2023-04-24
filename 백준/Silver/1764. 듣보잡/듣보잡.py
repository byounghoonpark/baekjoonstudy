n, m = map(int, input().split())
a = set()
b = set()
for i in range(n):
    a.add(input().rstrip())
for i in range(m):
    b.add(input().rstrip())
c = sorted(a.intersection(b))
print(len(c))
for i in c:
    print(i)