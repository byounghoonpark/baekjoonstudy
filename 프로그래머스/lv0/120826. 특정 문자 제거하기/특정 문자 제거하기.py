def solution(my_string, letter):
    a = []
    for i in my_string :
        if i != letter:
            a.append(i)
    answer = ''.join(str(i) for i in a)
    return answer