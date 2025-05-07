import sys

input = sys.stdin.readline

N, M = map(int, input().split())
numbers = list(map(int, input().split()))
sumnum = [0]
temp = 0

for i in numbers:
    temp = temp + i
    sumnum.append(temp)

for i in range(M):
    s, e = map(int, input().split())
    print(sumnum[e] - sumnum[s - 1])
