N,M,cy,cx,K = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]
lst = list(map(int, input().split()))

n1=n2=n3=n4=n5=n6=0 
alst = []

dy = [0,0,0,-1,1]
dx = [0,1,-1,0,0]

for dr in lst:
    ny,nx = cy+dy[dr], cx+dx[dr]
# 1. 범위 체크
    if 0<=ny<N and 0<=nx<M:
    # 2. 주사위 굴리기
        if dr == 1: # 동
            n1,n3,n4,n6 = n4,n1,n6,n3
        elif dr == 2:  # 서
            n1,n3,n4,n6 = n3,n6,n1,n4
        elif dr == 3:  # 북
            n1,n2,n5,n6 = n5,n1,n6,n2
        else: # 남
            n1,n2,n5,n6 = n2,n6,n1,n5
    # 3-1. 지도 값이 0이면, 지도 값 = 주사위 바닥 값
        if arr[ny][nx]==0:
            arr[ny][nx]=n6
    # 3-2. 0이 아니면 주사위 바닥 값 = 지도 값, 지도 값도 0으로
        else:
            n6 = arr[ny][nx]
            arr[ny][nx]=0
    # 4. 윗면 값 추가
        alst.append(n1)
    # 5. 좌표 이동
        cy,cx = ny,nx

for i in alst:
    print(i)