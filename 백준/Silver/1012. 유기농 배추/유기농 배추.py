from collections import deque

def bfs(y,x):
    q = deque()
    q.append([y,x])
    visited[y][x]=1
    directy = [-1,0,0,1]
    directx = [0,-1,1,0]
    while q:
        # 1이면 큐에 추가
        y,x=q.popleft()
        for i in range(4):
            dy=y+directy[i]
            dx=x+directx[i]
            if dy<0 or dx<0 or dy>=n or dx>=m:continue
            if arr[dy][dx] == 1 and visited[dy][dx] != 1:
                visited[dy][dx] = 1
                q.append([dy,dx])
    return

t = int(input())
for _ in range(t):
    m,n,k = map(int, input().split())
    arr = [[0]*m for _ in range(n)]
    visited = [[0]*m for _ in range(n)]
    for _ in range(k):
        x,y = map(int, input().split())
        arr[y][x]=1

    # 1일 때 탐색 시작
    cnt=0
    for i in range(n):
        for j in range(m):
            if arr[i][j]==1 and visited[i][j]!=1:
                bfs(i,j)
                cnt+=1

    print(cnt)