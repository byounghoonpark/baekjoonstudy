test = []
for i in range(30):
    test.append(i+1)
for _ in range(28):
    n = int(input())
    test.remove(n)
test.sort()
print(test[0])
print(test[1])