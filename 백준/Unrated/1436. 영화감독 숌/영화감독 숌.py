n = int(input())
a = 666
b = 0
while True:
    if '666' in str(a):
        b += 1
    if b == n:
        print(a)
        break
    a += 1