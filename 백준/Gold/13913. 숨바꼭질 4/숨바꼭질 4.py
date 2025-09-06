from collections import deque
import sys

input = sys.stdin.readline
n,k = map(int, input().split())

MAX = 100000
visited = [False]*(MAX+1)
parent = [-1]*(MAX+1)

q = deque()
q.append((n,0))
visited[n]=True

while q:
    now, cnt = q.popleft()
    if now==k:
        print(cnt)
        path = []
        cur = k
        while cur != -1:
            path.append(cur)
            cur = parent[cur]
        print(*path[::-1])
        break

    for next in (now-1,now+1, now*2):
        if 0<=next<=MAX and not visited[next]:
            visited[next]=True
            parent[next]=now
            q.append((next,cnt+1))