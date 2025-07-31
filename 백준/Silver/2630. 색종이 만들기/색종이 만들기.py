import sys
input = sys.stdin.readline

def cut(y,x,n):
    global white, blue
    color = paper[y][x]

    for i in range(y,y+n):
        for j in range(x,x+n):
            if color != paper[i][j]:
                cut(y,x,n//2) # 2사분면
                cut(y,x+n//2,n//2) # 1사분면
                cut(y+n//2, x, n//2) # 3사분면
                cut(y+n//2, x+n//2, n//2) # 4사분면
                return
    if color == 0:
        white+=1
    else:
        blue+=1
n = int(input())
paper = [list(map(int, input().split())) for _ in range(n)]

white, blue = 0,0
cut(0,0,n)
print(white, blue, sep='\n')