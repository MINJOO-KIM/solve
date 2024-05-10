from collections import deque
def bfs(y,x,h):
    q = deque()
    q.append([y,x])
    visited[y][x]=1

    while q:
        nowy,nowx = q.popleft()
        visited[nowy][nowx]=1

        directy = [-1,0,0,1]
        directx = [0,-1,1,0]

        for i in range(4):
            dy = nowy+directy[i]
            dx = nowx+directx[i]

            if dy<0 or dx<0 or dy>=N or dx>=N: continue
            if visited[dy][dx]==1: continue
            if arr[dy][dx]>h:
                q.append([dy,dx])
                visited[dy][dx]=1
# 영역 개수 세기
def solve(h):
    cnt=0
    for i in range(N):
        for j in range(N):
            if visited[i][j]==0 and arr[i][j]>h:
                bfs(i,j,h)
                cnt+=1
    return cnt

N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]
ans=0
for h in range(100):
    visited = [[0]*N for _ in range(N)]
    ans = max(ans,solve(h))
print(ans)
