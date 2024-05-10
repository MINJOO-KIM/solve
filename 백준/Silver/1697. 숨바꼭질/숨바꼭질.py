from collections import deque
A,B = map(int, input().split())
used = [0]*100001
q = deque()
q.append([A,0])

ans=0
while q:
    x, cnt = q.popleft()
    if x < 0 or x > 100000: continue
    if used[x]!=0:
        continue
    else:
        used[x]=1
        q.append([x - 1, cnt + 1])
        q.append([x + 1, cnt + 1])
        q.append([x * 2, cnt + 1])
    if x==B:
        ans=cnt
        break

print(ans)