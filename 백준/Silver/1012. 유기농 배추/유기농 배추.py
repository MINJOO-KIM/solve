import sys
from collections import deque
input = sys.stdin.readline
for _ in range(int(input())):
    m,n,k = map(int, input().split())
    lst = [[0]*m for _ in range(n)]

    for _ in range(k):
        j,i = map(int, input().split())
        lst[i][j]=1
    cnt=0

    def bfs(y,x):
        global cnt
        dy = [-1,0,0,1]
        dx = [0,-1,1,0]

        q = deque()
        q.append((y,x))
        while q:
            y,x = q.popleft()
            for i in range(4):
                ny = y+dy[i]
                nx = x+dx[i]
                if 0<=ny<n and 0<=nx<m and not visited[ny][nx] and lst[ny][nx]==1:
                    visited[ny][nx]=True
                    q.append((ny,nx))
        cnt+=1

    visited = [[False]*m for _ in range(n)]
    for i in range(n):
        for j in range(m):
            if lst[i][j]==1 and not visited[i][j]:
                bfs(i,j)
    print(cnt)