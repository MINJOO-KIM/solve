from collections import deque

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]
campus = []
ix, iy = 0, 0 
answer = 0

N, M = map(int, input().split()) 

for i in range(N):
    campus.append(list(input()))
    for j in range(M):
        if campus[i][j] == 'I': 
            ix, iy = i, j

visited = [[0] * M for _ in range(N)] 

deq = deque()
deq.append([ix, iy]) 

while deq:
    x, y = deq.popleft()
    for i in range(4):  
        nx, ny = x + dx[i], y + dy[i]
        if 0 <= nx < N and 0 <= ny < M and visited[nx][ny] == 0: 
            visited[nx][ny] = 1 
            if campus[nx][ny] == 'O':  
                deq.append([nx, ny])
            elif campus[nx][ny] == 'P':  
                deq.append([nx, ny])
                answer += 1 

print('TT' if answer == 0 else answer)