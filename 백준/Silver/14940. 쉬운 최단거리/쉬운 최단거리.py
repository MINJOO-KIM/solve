import sys
from collections import deque
input = sys.stdin.readline

n,m = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(n)]
# distance가 -1이 아니면 방문한거임!
distance = [[-1]*m for _ in range(n)]

gy = gx = -1
for i in range(n):
    for j in range(m):
        if graph[i][j]==2:
            gy,gx = i,j
            distance[i][j]=0
        elif graph[i][j]==0:
            distance[i][j]=0

# 목표지점부터 시작하기
q = deque([(gy, gx)]) # 행, 열
dy = [-1,0,0,1]
dx = [0,-1,1,0]

while q:
    y,x=q.popleft()
    for i in range(4):
        ny = y+dy[i]
        nx = x+dx[i]
        # 배열 범위 체크
        if 0 <= ny < n and 0 <= nx < m:
            # 탐색 가능 조건 (갈 수 있는 땅 and 아직 방문X)
                # 최단 거리 갱신 (어차피 BFS로 방문하면 그 칸에 도달할 수 있는 가장 빠른 거리)
            if graph[ny][nx] == 1 and distance[ny][nx] == -1:
                distance[ny][nx] = distance[y][x] + 1
                q.append((ny, nx))

for row in distance:
    print(*row)