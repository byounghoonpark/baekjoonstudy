n = []
for _ in range(10):
    a = int(input())
    n.append(int(a%42))
#set()함수를 이용해 중복제거
#len으로 set자료형의 길이 출력
print(len(set(n)))