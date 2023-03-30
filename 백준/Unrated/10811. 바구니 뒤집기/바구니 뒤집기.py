n, m = map(int, input().split())
box = []
for l in range (n):
    box.append(l+1)
for _ in range (m):
    i, j = map(int, input().split())
    while True:
        # 같은 순번끼린 바꿀게 없으니 break
        if j==i:
            break
        # 나머지에서 1 2를 입력 받았을 때 
        # 실제 인덱스값은 box[0], box[1]이니 -1씩 해서 치환 
        box[i-1],box[j-1] = box[j-1],box[i-1]
        # i와 j가 1 차이나면 상호 교환이니 break
        if j-i ==1:
            break
        # 2이상 차이날 시 ex) input(1 4) 이면 2,3번째 인덱스를 다시 교환
        else:
            j -= 1
            i += 1
print(*box)