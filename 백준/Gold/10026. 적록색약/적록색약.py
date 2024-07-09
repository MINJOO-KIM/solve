from collections import deque

n = int(input())
arr = [list(input()) for _ in range(n)]
visited = [[0]*n for _ in range(n)]
def BFS(i,j):
    q = deque()
    q.append([i,j])
    visited[i][j]=1

    while q:
        y,x = q.popleft()
        directy = [-1,0,0,1]
        directx = [0,-1,1,0]
        for i in range(4):
            dy = directy[i]+y
            dx = directx[i]+x
            if dy<0 or dx<0 or dy>=n or dx>=n: continue
            if visited[dy][dx]==1: continue
            if arr[dy][dx]==arr[y][x]:
                q.append([dy,dx])
                visited[dy][dx]=1
cnt=0
for i in range(n):
    for j in range(n):
        if visited[i][j]!=1:
            BFS(i,j)
            cnt+=1

visited = [[0] * n for _ in range(n)]
# 적록색약 처리 (R -> G로)
for i in range(n):
    for j in range(n):
        if arr[i][j]=='R':
            arr[i][j]='G'

cnt2=0
for i in range(n):
    for j in range(n):
        if visited[i][j]!=1:
            BFS(i,j)
            cnt2+=1
print(cnt, cnt2)