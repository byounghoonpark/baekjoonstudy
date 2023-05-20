def solution(cards1, cards2, goal):
    answer = []
    a = 0
    b = 0
    for j in goal:
        if a < len(cards1) and j == cards1[a]:
            answer.append(cards1[a])
            a += 1
            
        if b < len(cards2) and j == cards2[b]:
            answer.append(cards2[b])
            b += 1
    if answer == goal:
        return 'Yes'  
    else:
        return 'No'