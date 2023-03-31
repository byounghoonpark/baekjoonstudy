t = int(input())
for i in range(t):
    r,s = map(str, input().split())
    p = str()
    for j in range(len(s)):
        p += s[j]*int(r)
    print(p)