from collections import deque
import sys

input = sys.stdin.readline

n, m = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]

# 방향 설정
directy = [-1, 0, 0, 1]
directx = [0, -1, 1, 0]

def bfs(y, x, visited):
    q = deque()
    q.append((y, x))
    visited[y][x] = True
    while q:
        nowy, nowx = q.popleft()
        for d in range(4):
            dy = nowy + directy[d]
            dx = nowx + directx[d]
            if 0 <= dy < n and 0 <= dx < m:
                if arr[dy][dx] > 0 and not visited[dy][dx]:
                    visited[dy][dx] = True
                    q.append((dy, dx))

def melt():
    melt_list = []
    for i in range(n):
        for j in range(m):
            if arr[i][j] > 0:
                water = 0
                for d in range(4):
                    dy = i + directy[d]
                    dx = j + directx[d]
                    if 0 <= dy < n and 0 <= dx < m:
                        if arr[dy][dx] == 0:
                            water += 1
                if water > 0:
                    melt_list.append((i, j, water))
    for i, j, water in melt_list:
        arr[i][j] = max(0, arr[i][j] - water)

year = 0
while True:
    visited = [[False] * m for _ in range(n)]
    cnt = 0
    for i in range(n):
        for j in range(m):
            if arr[i][j] > 0 and not visited[i][j]:
                bfs(i, j, visited)
                cnt += 1
    if cnt == 0:
        print(0)
        break
    if cnt >= 2:
        print(year)
        break
    melt()
    year += 1
