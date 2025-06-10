n,m = map(int, input().split())
lst = [list(map(int, input().split())) for _ in range(n)]
temp = [[0]*m for _ in range(n)]
global answer
answer=0
dy = [-1,0,0,1]
dx = [0,-1,1,0]


def virus(y,x):
    for i in range(4):
        ny = y+dy[i]
        nx = x+dx[i]

        if 0<=ny<n and 0<=nx<m:
            if temp[ny][nx]==0:
                temp[ny][nx]=2
                virus(ny,nx)

# DFS로 울타리 설치하면서 개수 3개 됐을 때, 바이러스 전파/ 안전영역 최댓값 찾기
def dfs(count):
    # 울타리 3개 됐을 때,
    global answer
    if count==3:
        # temp 배열 세팅
        for i in range(n):
            for j in range(m):
                temp[i][j]=lst[i][j]
        # 전파 진행
        for i in range(n):
            for j in range(m):
                if temp[i][j]==2:
                    virus(i,j)
        # 안전영역 최댓값
        score = 0
        for i in range(n):
            for j in range(m):
                if temp[i][j] == 0:
                    score += 1
        if score>answer:
            answer=score
        return
    # 울타리 설치
    for i in range(n):
        for j in range(m):
            if lst[i][j]==0:
                lst[i][j]=1
                count+=1
                dfs(count)
                lst[i][j]=0
                count-=1

dfs(0)
print(answer)