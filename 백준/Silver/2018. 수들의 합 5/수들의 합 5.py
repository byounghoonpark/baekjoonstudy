n = int(input())
cnt = 1
st_idx = 1
ed_idx = 1
sum = 1

while ed_idx != n:
    if sum == n:
        cnt += 1
        ed_idx += 1
        sum += ed_idx
    elif sum > n:
        sum -= st_idx
        st_idx += 1
    else:
        ed_idx += 1 
        sum += ed_idx

print(cnt)