from collections import deque
n = int(input())
lines = [tuple(map(int, input().split())) for _ in range(n)]
lines.sort()

q = deque(lines)
start,end = q.popleft()
answer=0

while q:
    x,y=q.popleft()
    if x<=end: # 새로운 시작점이 현재 끝점보다 작으면 시작점 겹침!
        # 현재 시작점(start)~ 새로운 끝점(y)
        end = max(end,y)
    else: # 새로운 시작점이 끝점보다 크면 겹치지 않음!
        answer+=end-start
        start,end = x,y

answer+=end-start
print(answer)
