n = int(input())

a = []
for i in range(n):
    x, y = map(int, input().split())
    a.append([y, x])

a.sort()

for i in range(n):
    print(a[i][1],a[i][0])