import sys
input = sys.stdin.readline

n, m = map(int, input().split())
numbers = list(map(int, input().split()))
sum_num = [0]
temp = 0

for i in numbers:
    temp = temp+i
    sum_num.append(temp)
    
for i in range(m):
    a,b = map(int, input().split())
    print(sum_num[b]-sum_num[a-1])