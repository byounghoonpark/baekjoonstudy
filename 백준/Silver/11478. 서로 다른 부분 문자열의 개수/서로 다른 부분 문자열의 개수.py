import sys
input = sys.stdin.readline
s = input().rstrip()
a = set()
for i in range(len(s)):
   for j in range(i+1,len(s)+1):
      a.add(s[i:j])
print(len(a))