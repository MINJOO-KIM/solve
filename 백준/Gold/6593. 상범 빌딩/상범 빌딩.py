from collections import deque
import sys
input = sys.stdin.readline

while True:
    l,r,c = map(int, input().split())
    if l==0 and r==0 and c==0:
        break
    lst = []
    for _ in range(l):
        lst.append([list(map(str, input().rstrip())) for _ in range(r)])
        input()
    visited = [[[False]*c for _ in range(r)] for _ in range(l)]

    dz = [0,0,0,0,1,-1]
    dy = [1,-1,0,0,0,0]
    dx = [0,0,1,-1,0,0]

    def bfs(z,y,x):
        q = deque()
        q.append((z,y,x,0))

        while q:
            z,y,x,cnt = q.popleft()
            for i in range(6):
                nz = z+dz[i]
                ny = y+dy[i]
                nx = x+dx[i]
                if 0<=nz<l and 0<=ny<r and 0<=nx<c:
                    if lst[nz][ny][nx]=='.' and not visited[nz][ny][nx]:
                        visited[nz][ny][nx]=True
                        q.append((nz,ny,nx,cnt+1))
                    elif lst[nz][ny][nx]=='E' and not visited[nz][ny][nx]:
                        print(f'Escaped in {cnt + 1} minute(s).')
                        return
        print('Trapped!')

    for i in range(l):
        for j in range(r):
            for k in range(c):
                if lst[i][j][k]=='S':
                    visited[i][j][k]=True
                    bfs(i,j,k)