from collections import deque
n = int(input())
q = deque()
for i in range(1,n+1):
    q.append(i)
while len(q)>1:
    delete=q.popleft()
    move=q.popleft()
    q.append(move)
ans=q.popleft()
print(ans)