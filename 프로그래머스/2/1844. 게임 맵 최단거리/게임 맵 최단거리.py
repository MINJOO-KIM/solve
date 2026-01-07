from collections import deque
def solution(maps):
    answer = -1
    
    n = len(maps)
    m = len(maps[0])

    dy = [-1,0,0,1]
    dx = [0,-1,1,0]
    
    visited = [[False]*m for _ in range(n)]
        
    q = deque()
    q.append((0,0,1))
    visited[0][0]=True
    
    while q:
        y,x,cnt = q.popleft()
        if y==n-1 and x==m-1:
            answer = cnt

        for i in range(4):
            ny = y+dy[i]
            nx = x+dx[i]
            if 0<=ny<n and 0<=nx<m and not visited[ny][nx] and maps[ny][nx]!=0:
                visited[ny][nx]=True
                q.append((ny,nx,cnt+1))
            
    return answer