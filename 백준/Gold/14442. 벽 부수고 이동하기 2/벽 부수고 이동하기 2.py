import sys
input = sys.stdin.readline
from collections import deque

n,m,k = map(int, input().split())
graph = [list(map(int, input().rstrip())) for _ in range(n)]
visited = [[[0]*(k+1) for _ in range(m)] for _ in range(n)]
q = deque()
q.append((0,0,k))
visited[0][0][k]=1

dy = [-1,0,0,1]
dx = [0,-1,1,0]
def bfs():
    while q:
        y, x, k = q.popleft()
        if y==n-1 and x==m-1:
            return visited[y][x][k]
        for i in range(4):
            ny = y+dy[i]
            nx = x+dx[i]
            if 0<=ny<n and 0<=nx<m:
                if graph[ny][nx]==1 and k>0 and not visited[ny][nx][k-1]:
                    visited[ny][nx][k-1]=visited[y][x][k]+1
                    q.append((ny,nx,k-1))
                elif graph[ny][nx]!=1 and not visited[ny][nx][k]:
                    visited[ny][nx][k]=visited[y][x][k]+1
                    q.append((ny,nx,k))
    return -1

print(bfs())