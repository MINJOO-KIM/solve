import sys
from collections import deque
import copy

input = sys.stdin.readline
INF = int(1e9)

n,m = map(int, input().split())
graph = []
visited = [[False]*m for _ in range(n)]
distance = [[INF]*m for _ in range(n)]

for _ in range(n):
    arr = list(map(int, input().split()))
    graph.append(arr)


gy,gx = 0,0
for i in range(n):
    for j in range(m):
        if graph[i][j]==2:
            gy,gx = i,j
            distance[i][j]=0
        elif graph[i][j]==0:
            distance[i][j]=0

# 목표지점부터 시작하기
q = deque([[gy, gx, 0]]) # 행, 열, 최단거리

dy = [-1,0,0,1]
dx = [0,-1,1,0]

while q:
    y,x,dist=q.popleft()
    for i in range(4):
        ny = y+dy[i]
        nx = x+dx[i]
        # 배열 범위 체크
        if ny<0 or nx<0 or ny>=n or nx>=m:
            continue
        # 탐색 가능 조건 (아직 방문X, 갈 수 있는 땅)
            # 최단 거리 갱신
        if not visited[ny][nx] and graph[ny][nx]==1:
            visited[ny][nx]=True
            distance[ny][nx]= min(distance[ny][nx],dist+1)
            q.append([ny,nx,distance[ny][nx]])

# 원래 갈 수 있는데 아예 도달하지 못한 곳 -1 넣기
for i in range(n):
    for j in range(m):
        if not visited[i][j] and graph[i][j]==1:
            distance[i][j]=-1

for a in range(n):
    print(*distance[a])