import sys
from collections import deque
input = sys.stdin.readline
def D(n):
    return (n*2)%10000
def S(n):
    return 9999 if n==0 else n-1
def L(n):
    s = str(n).zfill(4)
    return int(s[1:]+s[0])
def R(n):
    s = str(n).zfill(4)
    return int(s[-1]+s[:-1])

def bfs(a,b):
    visited = [False]*10000
    q = deque()
    q.append((a,""))
    visited[a]=True

    while q:
        num,ans = q.popleft()
        if num==b:
            return ans

        next = D(num)
        if not visited[next]:
            visited[next]=True
            q.append((next,ans+'D'))

        next = S(num)
        if not visited[next]:
            visited[next] = True
            q.append((next, ans + 'S'))

        next = L(num)
        if not visited[next]:
            visited[next] = True
            q.append((next, ans + 'L'))

        next = R(num)
        if not visited[next]:
            visited[next] = True
            q.append((next, ans + 'R'))

result = []
for _ in range(int(input())):
    a,b = map(int, input().split())
    result.append(bfs(a,b))

print('\n'.join(result))