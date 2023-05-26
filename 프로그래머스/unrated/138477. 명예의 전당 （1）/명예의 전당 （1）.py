def solution(k, score):
    a=[]
    result = []
    for i in score:
        a.append(i)
        if len(result) < k:
            result.append(min(a))
        else:
            a.sort(reverse=True)
            result.append(a[k-1])
    return result