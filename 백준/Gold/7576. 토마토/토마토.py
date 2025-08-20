import sys
from collections import deque
m,n = map(int, input().split())
lst = [list(map(int, input().split())) for _ in range(n)]
visited = [[False]*m for _ in range(n)]

q = deque()

for i in range(n):
    for j in range(m):
        if lst[i][j]==1 and not visited[i][j]:
            q.append((i,j,0))
            visited[i][j]=True

dy = [-1,0,0,1]
dx = [0,-1,1,0]
ans = 0

while q:
    y,x,cnt = q.popleft()
    ans = max(ans,cnt)
    for i in range(4):
        ny = y+dy[i]
        nx = x+dx[i]
        if 0<=ny<n and 0<=nx<m and not visited[ny][nx] and lst[ny][nx]==0:
            visited[ny][nx]=True
            lst[ny][nx]=1
            q.append((ny,nx,cnt+1))
flag=0
for i in range(n):
    for j in range(m):
        if lst[i][j]==0:
            flag=1

if flag:
    print(-1)
else:
    print(ans)
