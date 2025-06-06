board = []
for _ in range(5):
    board.append(list(map(int, input().split())))

speak = []
for _ in range(5):
    speak.append(list(map(int, input().split())))

bingo = [[0]*5 for _ in range(5)]

def check_row():
    res = 0
    for i in range(5):
        cnt = 0
        for j in range(5):
            if bingo[i][j]==1:
                cnt+=1
        if cnt==5:
            res+=1
    return res

def check_col():
    res = 0
    for i in range(5):
        cnt = 0
        for j in range(5):
            if bingo[j][i]==1:
                cnt+=1
        if cnt==5:
            res+=1
    return res

def check_dia():
    res = 0
    # 오 -> 왼
    cnt=0
    for i in range(5):
        if bingo[i][4-i]==1:
            cnt+=1
    if cnt==5:
        res+=1
    # 왼 -> 오
    cnt=0
    for i in range(5):
        if bingo[i][i]==1:
            cnt+=1
    if cnt==5:
        res+=1
    return res

for i in range(5):
    for j in range(5):
        s = speak[i][j]
        for y in range(5):
            for x in range(5):
                if board[y][x]==s:
                    cnt=0
                    bingo[y][x]=1
                    cnt+=check_row()
                    cnt+=check_col()
                    cnt+=check_dia()
                    if cnt>=3:
                        print(i*5+j+1)
                        exit()
