def gcd(x,y):
    x,y=min(x, y),max(x, y)
    while x != 0:
        y = y%x 
        x,y = y,x
    return y

a,b = map(int,input().split())
c,d = map(int,input().split())

l = b*d//gcd(b,d) #최소공배수
n = a * (l // b) + c * (l // d)
g = gcd(n, l)

print(n // g, l // g)