n = int(input())

for i in range(1, n+1):   
    a = sum((map(int, str(i)))) 
    b = i + a  
    if b == n:
        print(i)
        break
    if i == n:
        print(0)