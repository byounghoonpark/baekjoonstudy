def solution(cards1, cards2, goal):
    answer = []
    a = b = 0
    for i in goal:
        if a < len(cards1) and i == cards1[a]:
            answer.append(cards1[a])
            a += 1
            
        if b < len(cards2) and i == cards2[b]:
            answer.append(cards2[b])
            b += 1
        
    return 'Yes' if answer == goal else 'No'