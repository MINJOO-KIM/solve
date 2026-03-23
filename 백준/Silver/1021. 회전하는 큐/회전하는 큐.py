from collections import deque
import sys
input = sys.stdin.readline
n,m = map(int, input().split())
targets = map(int, input().split())
ans = 0

q = deque()
for i in range(1,n+1):
    q.append(i)

for target in targets:
    target_index = q.index(target)
    while q[0]!=target:
        if target_index <= len(q)-target_index:
            q.append(q.popleft())
            ans+=1
        else:
            q.appendleft(q.pop())
            ans+=1
    q.popleft()
print(ans)
