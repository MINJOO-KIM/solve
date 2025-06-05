from collections import deque

N, K = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(N)]
visited = [[0] * N for _ in range(N)]
S, X, Y = map(int, input().split())

q = deque()
for virus in range(1, K + 1):
    for i in range(N):
        for j in range(N):
            if graph[i][j] == virus:
                q.append((virus, 0, i, j))
                visited[i][j] = 1

dy = [-1, 0, 0, 1]
dx = [0, -1, 1, 0]

while q:
    virus, day, y, x = q.popleft()
    if day == S:
        # S초가 되었으면 더 이상 퍼뜨리지 않음
        break

    for i in range(4):
        ny = y + dy[i]
        nx = x + dx[i]
        if 0 <= ny < N and 0 <= nx < N:
            if visited[ny][nx] == 0 and graph[ny][nx] == 0:
                graph[ny][nx] = virus
                visited[ny][nx] = 1
                q.append((virus, day + 1, ny, nx))

# BFS 종료 후에 결과 출력
print(graph[X - 1][Y - 1])
