import sys
from collections import deque
input = sys.stdin.readline

m,n,h = map(int, input().split())
lst = [[list(map(int, input().split())) for _ in range(n)] for _ in range(h)]
visited = [[[False]*m for _ in range(n)] for _ in range(h)]
flag=False
for k in range(h):
    for i in range(n):
        for j in range(m):
            if lst[k][i][j]==0:
                flag=True
dz = [-1,1,0,0,0,0]
dy = [0,0,-1,1,0,0]
dx = [0,0,0,0,-1,1]
q = deque()

if flag:
    for k in range(h):
        for i in range(n):
            for j in range(m):
                if lst[k][i][j]==1:
                    q.append((k,i,j))
                    visited[k][i][j] = True
    while q:
        z, y, x = q.popleft()
        for i in range(6):
            nz, ny, nx = z + dz[i], y + dy[i], x + dx[i]
            if 0 <= nz < h and 0 <= ny < n and 0 <= nx < m and not visited[nz][ny][nx] and lst[nz][ny][nx]==0:
                visited[nz][ny][nx] = True
                lst[nz][ny][nx]=lst[z][y][x]+1
                q.append((nz, ny, nx))
    flag_final=False
    for k in range(h):
        for i in range(n):
            for j in range(m):
                # bfs 수행했지만 토마토가 익지 않았을 때
                if lst[k][i][j] == 0:
                    flag_final = True
    if flag_final:
        print(-1)
    # 토마토 모두 익었다면 최댓값 출력하기
    else:
        ans=0
        for k in range(h):
            for i in range(n):
                for j in range(m):
                    ans=max(ans,lst[k][i][j])
        print(ans-1)
# 처음부터 모든 토마토가 익어있으면 (0이 없다면)
else:
    print(0)