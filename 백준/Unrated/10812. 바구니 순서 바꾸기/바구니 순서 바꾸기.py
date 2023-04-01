n,m = map(int, input().split())
b = []
for i in range (n) :
    b.append(int(i+1))
for a in range (1,m+1) :
    i,j,k = map(int, input().split())
    b = b[:i-1] + b[k-1:j] + b[i-1:k-1] + b[j:]
print(*b)
