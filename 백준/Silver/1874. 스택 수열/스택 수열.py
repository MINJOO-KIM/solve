import sys
input = sys.stdin.readline
n = int(input())
targets = []

for _ in range(n):
    targets.append(int(input()))
s = []
ans = []

current = 1
flag = 1

for target in targets:
    while current<=target:
        s.append(current)
        current+=1
        ans.append('+')

    if s[-1] == target:
        if s:
            s.pop()
            ans.append('-')

    else:
        flag = 0
        break
if flag:
    for i in range(len(ans)):
        print(ans[i])
else:
    print("NO")
