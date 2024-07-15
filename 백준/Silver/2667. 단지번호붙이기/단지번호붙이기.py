# bfs 함수 돌아서 cnt 뽑기
    # 함수 나오면 리스트에 house 넣기 + cnt 증가하기
from collections import deque
N = int(input())
arr = [list(map(int, input())) for _ in range(N)]
visited=[[0]*N for _ in range(N)]
ans=[]

def bfs(i,j):
    q = deque()
    house = 1
    q.append([i,j])
    visited[i][j]=1
    while q:
        y,x = q.popleft()
        for i in range(4):
            directy=[-1,0,0,1]
            directx=[0,-1,1,0]
            dy = y + directy[i]
            dx = x + directx[i]
            if dy<0 or dx<0 or dy>=N or dx>=N: continue
            if visited[dy][dx]==1: continue
            if arr[dy][dx]==1:
                q.append([dy,dx])
                visited[dy][dx]=1
                house+=1
    return house

cnt=0
# 1이 있으면 탐색 시작
for i in range(N):
    for j in range(N):
        if arr[i][j]==1 and visited[i][j]==0:
            ans.append(bfs(i,j))
            cnt+=1

print(cnt)
ans.sort()
for i in range(len(ans)):
    print(ans[i])