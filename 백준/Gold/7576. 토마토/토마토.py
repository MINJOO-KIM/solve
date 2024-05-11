from collections import deque
M,N = map(int, input().split())
arr = [list(map(int, input().split()))for _ in range(N)]
used = [[0]*M for _ in range(N)]

q = deque()
for i in range(N):
    for j in range(M):
        if arr[i][j]==1:
            q.append([i,j,0])

while q:
    y,x,cnt = q.popleft()
    directy = [-1,0,0,1]
    directx = [0,-1,1,0]

    for i in range(4):
        dy = y + directy[i]
        dx = x + directx[i]

        if dy<0 or dx<0 or dy>=N or dx>=M: continue
        if arr[dy][dx]==-1: continue
        if used[dy][dx]==1: continue
        if arr[dy][dx]==0:
            arr[dy][dx]=1
            used[dy][dx]=1
            q.append([dy,dx,cnt+1])

flag=0
for i in range(N):
    for j in range(M):
        if arr[i][j]==0:
            flag=1
if flag:
    print(-1)
else:
    print(cnt)