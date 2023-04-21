import sys
input = sys.stdin.readline
n = int(input())
a = list(map(int, input().split()))
m = int(input())
b = list(map(int, input().split()))

d = {a[i]:0 for i in range(len(a))}
#for i in range(len(a)):
#    d[a[i]] = 0  

for j in range(m):
    if b[j] not in d:
        print(0, end=' ')
    else:
        print(1, end=' ')