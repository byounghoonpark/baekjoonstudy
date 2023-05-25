def solution(s):
    answer = []
    a = {}
    for i, j in enumerate(list(s)):
        if j not in a:
            answer.append(-1)
            a[j] = i
        else:
            answer.append(i - a[j])
            a[j] = i
    return answer