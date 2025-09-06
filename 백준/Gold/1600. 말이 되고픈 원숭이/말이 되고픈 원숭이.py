from collections import deque
import sys
k = int(input())
m,n = map(int, input().split())
lst = [list(map(int, input().split())) for _ in range(n)]

hy = [-2,-2,-1,-1,1,1,2,2]
hx = [-1,1,-2,2,-2,2,-1,1]
dy = [-1,0,0,1]
dx = [0,-1,1,0]

visited = [[[0]*(k+1) for _ in range(m)] for _ in range(n)]
visited[0][0][k]=True
q = deque()
q.append((0,0,k,0)) #y,x,k,cnt

def bfs():
    while q:
        y,x,k,cnt = q.popleft()
        if y==n-1 and x==m-1:
            return cnt

        if k>0:
            for i in range(8):
                ny = y+hy[i]
                nx = x+hx[i]
                if 0<=ny<n and 0<=nx<m:
                    if lst[ny][nx]!=1 and not visited[ny][nx][k-1]:
                        visited[ny][nx][k-1]=True
                        q.append((ny,nx,k-1,cnt+1))
        for i in range(4):
            ny = y+dy[i]
            nx = x+dx[i]
            if 0 <= ny < n and 0 <= nx < m:
                if lst[ny][nx] != 1 and not visited[ny][nx][k]:
                    visited[ny][nx][k]=True
                    q.append((ny, nx, k, cnt + 1))
    return -1

print(bfs())