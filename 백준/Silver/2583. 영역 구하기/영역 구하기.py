from collections import deque

m,n,k = map(int, input().split())
graph = [[0]*n for _ in range(m)]


def bfs(i, j):
    q = deque()
    q.append((i, j))
    dx = [0, 0, -1, 1]
    dy = [1, -1, 0, 0]
    cnt = 1
    while q:
        y, x = q.popleft()
        for i in range(4):
            ny = y+dy[i]
            nx = x+dx[i]
            if 0 <= ny < m and 0 <= nx < n and graph[ny][nx] == 0:
                graph[ny][nx] = 1
                q.append((ny, nx))
                cnt += 1
    return cnt


for _ in range(k):
    x1, y1, x2, y2 = map(int, input().split())
    for i in range(y1, y2):
        for j in range(x1, x2):
            graph[i][j] += 1

ans = []

for i in range(m):
    for j in range(n):
        if graph[i][j] == 0:
            graph[i][j] += 1
            ans.append(bfs(i, j))

print(len(ans))
print(*sorted(ans))