import sys
input = sys.stdin.readline
n,m = map(int, input().split())
a={}
for i in range(1,n+1):
    name = input().rstrip()
    a[name] = i
    a[i] = name
for i in range(m):
    dogam = input().rstrip()
    if dogam.isdigit():
        print(a[int(dogam)])
    else:
        print(a[dogam])