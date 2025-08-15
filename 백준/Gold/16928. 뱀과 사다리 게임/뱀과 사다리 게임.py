from collections import deque
import sys

input = sys.stdin.readline
n,m = map(int, input().split())
board = [i for i in range(101)]
for _ in range(n):
    x,y = map(int, input().split())
    board[x]=y
for _ in range(m):
    u,v = map(int, input().split())
    board[u]=v

visited = [False]*101
q = deque()
q.append((1,0))
visited[1]=True

while q:
    cur,cnt = q.popleft()
    if cur==100:
        print(cnt)
        break
    for dice in range(1,7):
        next = cur+dice
        if next<=100:
            next = board[next] # 사다리/뱀 이동 고려
            if not visited[next]:
                visited[next]=True
                q.append((next,cnt+1))

