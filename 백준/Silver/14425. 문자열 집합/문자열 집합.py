import sys
input = sys.stdin.readline

d = {}
cnt = 0
n, m = map(int, input().split())

for _ in range(n):
    data = input()
    d[data] = True #임의의 value값임

for _ in range(m):
    data = input()
    if data in d:
        cnt += 1

print(cnt)