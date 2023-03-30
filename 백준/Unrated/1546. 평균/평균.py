n = int(input())
test = list(map(int, input().split()))
m = max(test)

new = []
for i in test :
    new.append(i/m *100)
print(sum(new)/n)