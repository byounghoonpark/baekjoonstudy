n = int(input())

a = []
for i in range (n):
    x,y = map(str, input().split())
    a.append([int(x), i, y])
a.sort()
for i in range (n):
    print(a[i][0],a[i][2])