from collections import deque

n,l,r = map(int, input().split())
lst = [list(map(int, input().split())) for _ in range(n)]


dy = [-1,0,0,1]
dx = [0,-1,1,0]


# 연합찾기 (BFS)
def check(i,j,index):
    group_info = []  # 현재 연합 정보를 담는 리스트
    group_num[i][j]=index # 연합 번호

    group_info.append((i,j))
    q = deque()
    q.append((i,j))
    cnt = 1
    total = lst[i][j]

    while q:
        y,x = q.popleft()
        for i in range(4):
            ny = y+dy[i]
            nx = x+dx[i]
            # 배열 범위 조건
            if ny<0 or nx<0 or ny>=n or nx>=n: continue
            # 상하좌우 비교, l과 r사이면 연합배열, 탐색 큐에 추가
            if l<=abs(lst[ny][nx]-lst[y][x])<=r and group_num[ny][nx]==-1:
                group_info.append((ny, nx)) # 연합 배열 추가
                group_num[ny][nx] = index # 연합 번호 갱신 (이미 탐색했음을 알려줌)
                q.append((ny,nx))
                # 연합 국가 개수, 연합 국가 총 인원수도 계속 갱신
                cnt+=1 # 연합 국가 개수
                total+=lst[ny][nx] # 연합 국가 총 인원 수

    # 연합찾기 끝났으면 인구이동 시작
    for gy,gx in group_info:
        lst[gy][gx]=int(total//cnt)



# 인구 이동할 수 없을 때까지 반복

answer = 0

# 인구 이동 계속 반복
while True:
    group_num = [[-1] * n for _ in range(n)]  # 연합 번호
    index = 0  # 연합 번호 시작
    for i in range(n):
        for j in range(n):
            if group_num[i][j]==-1: # 아직 연합 여부 체크 못한 국가라면
                check(i,j,index)
                index+=1
    if index == n*n:
        break
    answer+=1

print(answer)
