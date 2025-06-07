from itertools import combinations

n = int(input()) 
board = [] 
teachers = [] # 선생님 위치 정보
spaces = [] # 빈 공간 위치 정보

for i in range(n):
    board.append(list(input().split()))
    for j in range(n):
        if board[i][j] == 'T':
            teachers.append((i, j))
        if board[i][j] == 'X':
            spaces.append((i, j))

def watch(x, y, direction):
    # 왼쪽 방향
    if direction == 0:
        while y >= 0:
            if board[x][y] == 'S': 
                return True
            if board[x][y] == 'O': 
                return False
            y -= 1
    # 오른쪽 방향
    if direction == 1:
        while y < n:
            if board[x][y] == 'S': 
                return True
            if board[x][y] == 'O': 
                return False
            y += 1
    # 위쪽 방향
    if direction == 2:
        while x >= 0:
            if board[x][y] == 'S': 
                return True
            if board[x][y] == 'O': 
                return False
            x -= 1
    # 아래쪽 방향
    if direction == 3:
        while x < n:
            if board[x][y] == 'S': 
                return True
            if board[x][y] == 'O': 
                return False
            x += 1
    return False

# 장애물 설치 이후에, 한 명이라도 학생이 감지되는지 검사
def process():
    for x, y in teachers:
        for i in range(4):
            if watch(x, y, i):
                return True
    return False

find = False # 설치 성공 여부

for data in combinations(spaces, 3):
    # 장애물들을 설치해보기
    for x, y in data:
        board[x][y] = 'O'
    # 학생이 한 명도 감지되지 않는 경우
    if not process():
        find = True
        break
    # 설치된 장애물을 다시 없애기
    for x, y in data:
        board[x][y] = 'X'

if find:
    print('YES')
else:
    print('NO')