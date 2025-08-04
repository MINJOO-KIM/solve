import sys
from collections import deque
n,m = map(int, input().split())
lst = [list(map(str, input())) for _ in range(n)]
visited = [[False]*m for _ in range(n)]
dy = [-1,0,0,1]
dx = [0,-1,1,0]

cnt=0

def bfs(i,j):
    global cnt
    q = deque()
    q.append((i,j))

    while q:
        y,x = q.popleft()
        for i in range(4):
            ny = y+dy[i]
            nx = x+dx[i]

            if 0<=ny<n and 0<=nx<m and not visited[ny][nx]:
                visited[ny][nx]=True
                if lst[ny][nx]=='O':
                    q.append((ny,nx))
                elif lst[ny][nx]=='P':
                    q.append((ny,nx))
                    cnt+=1

for i in range(n):
    for j in range(m):
        if lst[i][j]=='I':
            sy,sx = i, j
            bfs(sy,sx)

if cnt==0:
    print('TT')
else:
    print(cnt)