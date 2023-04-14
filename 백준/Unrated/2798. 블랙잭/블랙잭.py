n,m = map(int,input().split())
a = list(map(int, input().split()))
b = 0
for i in range(n):
    for j in range(i+1,n):
        for k in range(j+1,n):
            sum = a[i]+a[j]+a[k]
            if sum <= m:
                b = max(b,sum)
print(b)