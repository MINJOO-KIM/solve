import sys
input = sys.stdin.readline
from collections import deque
def melt(lst):
    # melt 함수에서 바로 값을 바꿔버리면 제대로 반영X
        # melt_lst를 따로 관리
    melt_lst = [[0]*m for _ in range(n)]
    for y in range(n):
        for x in range(m):
            if lst[y][x]>0:
                ocean=0
                for i in range(4):
                    ny=y+dy[i]
                    nx=x+dx[i]
                    # 방향배열 체크 (접해있는 면 개수만큼 빼서 저장)
                    if 0<=ny<n and 0<=nx<m:
                        if lst[ny][nx]==0:
                            ocean+=1
                melt_lst[y][x]=max(0,lst[y][x]-ocean)
    return melt_lst
def cnt_ice(y,x):
    q = deque()
    q.append((y,x))
    visited[y][x]=True

    while q:
        y, x = q.popleft()
        for i in range(4):
            ny = y + dy[i]
            nx = x + dx[i]
            if 0 <= ny < n and 0 <= nx < m and not visited[ny][nx]:
                if lst[ny][nx]>0:
                    visited[ny][nx]=True
                    q.append((ny,nx))

# 빙산 녹이기 -> 개수 세기
n,m = map(int, input().split())
lst = [list(map(int, input().split())) for _ in range(n)]

dy = [-1,0,0,1]
dx = [0,-1,1,0]

# cnt 2개인 최초의 시간을 출력
# 다 녹을 때까지 분리 되지 않으면 0 출력
time=1
while True:
    lst = melt(lst) # 빙산 먼저 녹이기
    # visited는 개수 셀 때마다 초기화
    visited = [[False] * m for _ in range(n)]
    cnt = 0
    for i in range(n):
        for j in range(m):
            if lst[i][j]>0 and not visited[i][j]:
                cnt_ice(i,j)
                cnt+=1
    if cnt==0:
        print(0)
        break
    if cnt>=2:
        print(time)
        break
    time+=1
