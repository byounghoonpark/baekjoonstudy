test = []
for i in range(30):
    test.append(i+1)
for _ in range(28):
    n = int(input())
    
# remove()함수로 리스트 원소 직접 삭제
# del test[n] 이렇게 index로도 삭제 가능
    test.remove(n)
    
# 오름차순 정렬 == sort(reverse=False)
# sort(reverse=True) 이렇게 쓰면 내림차순 정렬 가능
test.sort()
print(test[0])
print(test[1])
