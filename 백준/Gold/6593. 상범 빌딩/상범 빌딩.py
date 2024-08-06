# bfs
    # 입력 받는게 새로운 bfs...!
        # 여러 빌딩 구분을 어떻게 하지...? (왜냐하면 빌딩들이 층마다 공백도 있고...입력끝만 알려줌...)
            # 일단 while:True로 실행 + 0 0 0이면 break
            # 빌딩 당 공백 -> input()으로 처리
    # 큐 추가 조건:
        # 배열범위
        # visited False고, arr[dz][dy][dx]=='.'
    # 가장 빨리 탈출하는 경우를 구하는거여서 E(도착)이면 바로 minute을 return해도 될듯..
        # bfs 함수써서
        # E(도착지점): return minute
        # 큐 끝날 때까지 (bfs 함수 끝날 때까지): return 0 (탈출실패)
    # 정답 출력하기
        # print 안에 변수 넣기... 까먹음
            # f-string => f'' 안에 {변수}
            # format => '' 안에 들어갈 변수 부분 {}로 나타내고 ''.format(변수)


from collections import deque
def bfs(sz,sy,sx):
    q = deque()
    q.append([sz,sy,sx,1])
    visited[sz][sy][sx]=1
    while q:
        z,y,x,minute = q.popleft()
        for i in range(6):
            nz = directz[i]+z
            ny = directy[i]+y
            nx = directx[i]+x

            if nz<0 or ny<0 or nx<0 or nz>=L or ny>=R or nx>=C: continue
            if arr[nz][ny][nx]=='#': continue
            if arr[nz][ny][nx]=='E':
                return minute
            if visited[nz][ny][nx]==0 and arr[nz][ny][nx]=='.':
                q.append([nz,ny,nx,minute+1])
                visited[nz][ny][nx]=1

# 3차원 배열, 방향 6
# L 층수(z) R 행(y) C 열(x)
directz = [-1,1,0,0,0,0]
directy = [0,0,1,-1,0,0]
directx = [0,0,0,0,1,-1]

while True:
    L,R,C = map(int,input().split())
    if (L,R,C) == (0,0,0): break

    # arr = [[list(map(int, input().split()) for _ in range(R))] for _ in range(L)]
    # print(arr)
    arr = []
    for i in range(L):
        floor = []
        for j in range(R):
            floor.append(list(input().strip()))
        arr.append(floor)
        input()  # 한줄 공백 제거
    visited = [[[0]*C for _ in range(R)] for _ in range(L)]

    # S 좌표 찾기
    for i in range(L):
        for j in range(R):
            for k in range(C):
                if arr[i][j][k]=='S':
                    ans=bfs(i,j,k)

    if ans==None:
        print("Trapped!")
    else:
        print(f"Escaped in {ans} minute(s).")
        # print("Escaped in {} minute(s).".format(ans))
