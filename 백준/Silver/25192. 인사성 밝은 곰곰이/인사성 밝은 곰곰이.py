n = int(input())
a = set()
cnt = 0
for i in range(n):
    b = input().rstrip()
    if b !='ENTER':
        if b not in a:
            cnt += 1
            a.add(b)
    else:
        a.clear()
print(cnt)