# bfs
    # 방향이 dy(N) dx(M) dz(H), 6방향
    # [(-1,0,0), (1,0,0), (0,1,0), (0,-1,0), (0,0,1), (0,0,-1)]

# 3차원 배열 입력받기

# 이동 조건
    # 방향배열로 체크해서
        # 배열범위 체크
        # 0 있으면 + used[dy,dx,dz]가 0이면 -> q에 추가

# 며칠걸리는지
    # max_cnt, cnt 비교 (큐에서 popleft할때마다)

from collections import deque

M, N, H = map(int, input().split())
arr = [[list(map(int, input().split())) for _ in range(N)] for _ in range(H)]
used = [[[0] * M for _ in range(N)] for _ in range(H)]
q = deque()

dz = [-1, 1, 0, 0, 0, 0]
dy = [0, 0, -1, 1, 0, 0]
dx = [0, 0, 0, 0, -1, 1]

for i in range(H):
    for j in range(N):
        for k in range(M):
            if arr[i][j][k] == 1:
                q.append((i, j, k, 0))
max_cnt =0
while q:
    z, y, x, cnt = q.popleft()
    max_cnt = max(max_cnt, cnt)
    for i in range(6):
        nz = z + dz[i]
        ny = y + dy[i]
        nx = x + dx[i]
        if 0 <= nz < H and 0 <= ny < N and 0 <= nx < M:
            if arr[nz][ny][nx] == 0 and used[nz][ny][nx] == 0:
                arr[nz][ny][nx] = 1
                used[nz][ny][nx] = 1
                q.append((nz, ny, nx, cnt + 1))

max_days = 0
flag = False
for i in range(H):
    for j in range(N):
        for k in range(M):
            if arr[i][j][k] == 0:
                flag = True
                break
        if flag:
            break
    if flag:
        break

if flag:
    print(-1)
else:
    print(max_cnt)
