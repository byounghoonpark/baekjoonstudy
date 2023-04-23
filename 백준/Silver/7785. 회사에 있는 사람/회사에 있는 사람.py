import sys
input = sys.stdin.readline
n = int(input())
a = {}
for i in range (n):
    name, work = map(str, input().split())
    a[name]=work

a = dict(sorted(a.items(), reverse=True))

for key,value in a.items():
    if value == 'enter':
        print(key)