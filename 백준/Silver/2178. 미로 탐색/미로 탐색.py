from collections import deque
N,M = map(int, input().split())
arr = [list(map(int, input())) for _ in range(N)]
used = [[0]*M for _ in range(N)]

ans=0
def bfs(y,x,cnt):
    q = deque()
    q.append([y,x,cnt])
    used[y][x]=1
    global ans

    while q:
        y,x,cnt = q.popleft()
        if y==N-1 and x==M-1:
            ans=cnt

        directy = [-1, 0, 0, 1]
        directx = [0, -1, 1, 0]
        for i in range(4):
            dy = y+directy[i]
            dx = x+directx[i]
            if 0 <= dy <= N-1 and 0 <= dx <= M-1 and arr[dy][dx] == 1 and used[dy][dx] == 0:
                used[dy][dx] = 1
                q.append([dy, dx, cnt + 1])
bfs(0,0,1)
print(ans)