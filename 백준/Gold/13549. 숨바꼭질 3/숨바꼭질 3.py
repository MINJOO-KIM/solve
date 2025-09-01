from collections import deque
import sys
input = sys.stdin.readline

n, k = map(int, input().split())
MAX = 100000
visited = [False]*(MAX+1)

q = deque()
q.append((n, 0))
visited[n] = True

while q:
    now, cnt = q.popleft()
    if now == k:
        print(cnt)
        break
    if 0 <= now * 2 <= MAX and not visited[now * 2]:
        visited[now * 2] = True
        q.appendleft((now * 2, cnt))

    for nxt in (now - 1, now + 1):
        if 0 <= nxt <= MAX and not visited[nxt]:
            visited[nxt] = True
            q.append((nxt, cnt + 1))
