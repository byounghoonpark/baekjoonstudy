import math
def solution(numer1, denom1, numer2, denom2):
    bunmo = denom1*denom2//math.gcd(denom1,denom2)
    bunja = numer1*bunmo//denom1+numer2*bunmo//denom2
    d = math.gcd(bunja, bunmo)
    answer = [bunja//d,bunmo//d]
    return answer 