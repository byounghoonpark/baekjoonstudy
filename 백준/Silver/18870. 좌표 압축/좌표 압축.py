import sys
input = sys.stdin.readline
n = int(input())
a = list(map(int,input().split()))
b = []

b = list(sorted(set(a)))

c = {b[i]:i for i in range (len(b))}

for i in a:
  print(c[i],end=' ')