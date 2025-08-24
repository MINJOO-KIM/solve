import sys
input = sys.stdin.readline
from collections import deque

for _ in range(int(input())):
    m,n = map(int, input().split())
    lst = [list(input()) for _ in range(n)]
    fire = deque()
    person = deque()

    fire_time = [[-1]*m for _ in range(n)]
    visited = [[0]*m for _ in range(n)]

    for i in range(n):
        for j in range(m):
            if lst[i][j]=='*':
                fire.append((i,j,0))
                fire_time[i][j]=0
            if lst[i][j]=='@':
                person.append((i,j,0))
                visited[i][j]=True

    dy = [-1,0,0,1]
    dx = [0,-1,1,0]

    flag=False

    while fire:
        y,x,cnt = fire.popleft()
        for i in range(4):
            ny = y+dy[i]
            nx = x+dx[i]
            if 0<=ny<n and 0<=nx<m and fire_time[ny][nx]==-1 and lst[ny][nx]!='#':
                fire_time[ny][nx]=cnt+1
                fire.append((ny,nx,cnt+1))
    while person:
        y,x,cnt = person.popleft()
        if y==0 or x==0 or y==n-1 or x==m-1:
            flag=True
            print(cnt+1)
            break
        for i in range(4):
            ny = y+dy[i]
            nx = x+dx[i]
            if 0<=ny<n and 0<=nx<m and lst[ny][nx]=='.' and not visited[ny][nx]:
                if fire_time[ny][nx]==-1 or cnt+1 < fire_time[ny][nx]:
                    visited[ny][nx]=True
                    person.append((ny,nx,cnt+1))

    if not flag:
        print('IMPOSSIBLE')