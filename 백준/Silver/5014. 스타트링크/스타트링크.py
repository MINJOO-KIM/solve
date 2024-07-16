from collections import deque
F,S,G,U,D = map(int, input().split())

# S에서 +1*U -1*D 해서 G가 될때까지 횟수 카운트
    # 큐에 넣고 visited에 횟수 업데이트
    # 큐에서 뺀게 G와 동일하면 최신 횟수 반환
    # G가 없으면 use the stairs 반환 (visited값 -1)

visited = [-1]*(F+1)

def bfs(start):
    q = deque()
    q.append(start)
    visited[start]=0

    while q:
        now = q.popleft()

        if now==G:
            return visited[now]

        for next in (now+U, now-D):
            if 0<next<=F and visited[next]==-1:
                visited[next]=visited[now]+1
                q.append(next)

    if visited[G]==-1:
        return "use the stairs"

print(bfs(S))
