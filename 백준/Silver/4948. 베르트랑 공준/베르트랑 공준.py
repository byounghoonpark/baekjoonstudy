import sys
input = sys.stdin.readline
def prime(n):
    if n ==1:
        return False
    for i in range(2,int(n**0.5)+1):
        if n%i==0:
            return False
    return True

all_list = set(range(2,246912))
is_prime = set()

for i in all_list:
    if prime(i):
        is_prime.add(i)

while True:
    cnt=0
    n = int(input())
    if n == 0 :
            break
    for i in is_prime:
        if n < i <=2*n:
            cnt+=1
    print(cnt)