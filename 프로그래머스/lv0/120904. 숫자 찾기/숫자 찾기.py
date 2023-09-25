def solution(num, k):
    answer = 0
    for i in str(num):
        if int(i) == k:
            break
        answer += 1
    else:
        return -1
    return answer + 1