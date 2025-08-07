import sys
input = sys.stdin.readline

n = int(input())
m = int(input())
s = input()

pn = 'IO'*(n)+'I'

answer = 0
for i in range(len(s)):
    if s[i]=='I':
        if s[i:i+len(pn)]==pn:
            answer+=1
print(answer)