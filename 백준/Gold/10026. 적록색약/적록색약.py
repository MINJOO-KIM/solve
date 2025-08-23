import sys
from collections import deque
input = sys.stdin.readline

n = int(input())
lst = [list(input()) for _ in range(n)]

visited = [[False]*n for _ in range(n)]
visited_rg = [[False]*n for _ in range(n)]

dy = [-1,0,0,1]
dx = [0,-1,1,0]
def bfs_rg(y,x):
    q = deque()
    q.append((y, x))

    while q:
        y, x = q.popleft()
        for i in range(4):
            ny = y + dy[i]
            nx = x + dx[i]
            if 0 <= ny < n and 0 <= nx < n and not visited_rg[ny][nx]:
                if lst[y][x] == 'B' and lst[ny][nx] == 'B':
                    visited_rg[ny][nx] = True
                    q.append((ny, nx))
                if lst[ny][nx] != 'B' and lst[y][x]!='B':
                    visited_rg[ny][nx] = True
                    q.append((ny, nx))
def bfs(y,x):
    q = deque()
    q.append((y,x))

    while q:
        y,x = q.popleft()
        for i in range(4):
            ny = y+dy[i]
            nx = x+dx[i]
            if 0<=ny<n and 0<=nx<n and not visited[ny][nx]:
                    if lst[y][x]==lst[ny][nx]:
                        visited[ny][nx]=True
                        q.append((ny,nx))

cnt_rg,cnt=0,0
for i in range(n):
    for j in range(n):
        if not visited_rg[i][j]:
            bfs_rg(i,j)
            cnt_rg+=1
        if not visited[i][j]:
            bfs(i,j)
            cnt+=1

print(cnt,cnt_rg)