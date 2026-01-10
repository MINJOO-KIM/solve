from collections import deque
def solution(rectangle, characterX, characterY, itemX, itemY):
    answer = 0
    graph = [[-1]*102 for _ in range(102)]
    visited = [[False]*102 for _ in range(102)]
    q = deque()
    
    dy = [-1,0,0,1]
    dx = [0,-1,1,0]
    
    for r in rectangle:
        x1,y1,x2,y2 = map(lambda x: x*2, r)
        for i in range(x1,x2+1):
            for j in range(y1,y2+1):
                if x1<i<x2 and y1<j<y2:
                    graph[i][j]=0
                elif graph[i][j]!=0:
                    graph[i][j]=1
    cx,cy,ix,iy = 2*characterX, 2*characterY, 2*itemX, 2*itemY
    q.append((cx,cy,0))
    visited[cx][cy]=True
    
    while q:
        x,y,cnt = q.popleft()
        if x==ix and y==iy:
            answer = cnt//2
        for i in range(4):
            nx = x+dx[i]
            ny = y+dy[i]
            if graph[nx][ny]==1 and not visited[nx][ny]:
                visited[nx][ny] = True
                q.append((nx,ny,cnt+1))
    return answer