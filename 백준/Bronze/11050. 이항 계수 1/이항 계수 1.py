import sys
from itertools import combinations
input = sys.stdin.readline
n,k = map(int, input().split())
nums = []
for i in range (n):
    nums.append(i)
a = list(combinations(nums,k))
print(len(a))