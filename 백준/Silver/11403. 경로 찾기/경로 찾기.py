import sys
from collections import deque
input = sys.stdin.readline

def bfs(start):
    q = deque()
    q.append(start)
    visited = [0]*n
    while q:
        now = q.popleft()
        for next in range(n):
            if graph[now][next]==1 and not visited[next]:
                visited[next]=1
                q.append(next)
    return visited

n = int(input())
graph = [list(map(int, input().split())) for _ in range(n)]

for i in range(n):
    graph[i]=bfs(i)

for row in graph:
    print(*row)
