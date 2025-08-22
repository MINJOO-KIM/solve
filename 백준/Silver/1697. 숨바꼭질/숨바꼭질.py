from collections import deque
import sys
input = sys.stdin.readline
n,k = map(int, input().split())
visited = [False]*100001

def plus(n):
    return n+1
def minus(n):
    return n-1
def double(n):
    return 2*n

q = deque()
q.append((n,0))
visited[n]=True

while q:
    now,cnt = q.popleft()
    if now==k:
        print(cnt)
        exit()
    now_p = plus(now)
    now_m = minus(now)
    now_d = double(now)
    if 0 <= now_p <= 100000 and not visited[now_p]:
        visited[now_p] = True
        q.append((now_p, cnt + 1))
    if 0 <= now_m <= 100000 and not visited[now_m]:
        visited[now_m] = True
        q.append((now_m, cnt + 1))
    if 0 <= now_d <= 100000 and not visited[now_d]:
        visited[now_d] = True
        q.append((now_d, cnt + 1))
