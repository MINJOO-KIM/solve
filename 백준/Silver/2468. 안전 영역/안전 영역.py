from collections import deque
def bfs(y,x,h):
    q = deque()
    q.append((y,x))
    visited[y][x]=1

    while q:
        y,x = q.popleft()
        visited[y][x]=1

        dy = [-1,0,0,1]
        dx = [0,-1,1,0]

        for i in range(4):
            ny = y+dy[i]
            nx = x+dx[i]

            if 0<=ny<n and 0<=nx<n and not visited[ny][nx]:
                if lst[ny][nx]>h:
                    q.append((ny,nx))
                    visited[ny][nx]=1
def solve(h):
    cnt=0
    for i in range(n):
        for j in range(n):
            if not visited[i][j] and lst[i][j]>h:
                bfs(i,j,h)
                cnt+=1
    return cnt

n = int(input())
lst = [list(map(int, input().split())) for _ in range(n)]
ans=0
for h in range(100):
    visited = [[0]*n for _ in range(n)]
    ans = max(ans,solve(h))
print(ans)
