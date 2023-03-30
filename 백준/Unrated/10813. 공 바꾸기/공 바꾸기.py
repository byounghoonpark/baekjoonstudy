n,m = map(int,input().split())
box = []
#append를 이용해서 box라는 list에 할당
for i in range(n):
    box.append(i+1)
# 입력받은 값을 서로 치환
# 예를들어 5 4 면 box[5]=box[4]
#               box[4]=box[5]
for _ in range (m) :
    i,j = map(int,input().split())
    box[i-1], box[j-1] = box[j-1], box[i-1]
# print(box) == [3, 1, 4, 2, 5]
# print(*box) == 3 1 4 2 5
print(*box)