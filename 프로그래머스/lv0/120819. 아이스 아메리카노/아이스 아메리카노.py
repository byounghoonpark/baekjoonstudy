def solution(money):
    a = money//5500
    b = money%5500
    answer = []
    answer.append(a)
    answer.append(b)
    return answer