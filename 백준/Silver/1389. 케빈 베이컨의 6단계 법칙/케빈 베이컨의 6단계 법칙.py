import sys
from collections import deque
input = sys.stdin.readline
n,m = map(int, input().split())
graph = [[] for _ in range(n+1)]

for _ in range(m):
    a,b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

def bfs(start):
    visited = [False] * (n + 1)
    total = 0
    q = deque()
    q.append((start,0))
    visited[start]=True

    while q:
        now,dist = q.popleft()
        total+=dist
        for neighbor in graph[now]:
            if not visited[neighbor]:
                visited[neighbor]=True
                q.append((neighbor,dist+1))

    return total

answer_dist = int(1e9)
answer_idx = 0
for i in range(1,n+1):
    if bfs(i)<answer_dist:
        answer_dist=min(bfs(i),answer_dist)
        answer_idx=i
print(answer_idx)
