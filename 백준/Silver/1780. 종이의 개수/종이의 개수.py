n = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]

cnt = []

# 분할정복
def divide(x,y,n):
    color = arr[x][y]

    # 색이 같은지
    for i in range(x,x+n):
        for j in range(y,y+n):

            # 색이 다르면 분할정복
            if color != arr[i][j]:
                for a in range(3):
                    for b in range(3):
                        divide(x+(n//3)*a, y+(n//3)*b, n//3)
                return

    # 색에 따라 cnt 증가
    if color == 1:
        cnt.append(1)
    elif color == -1:
        cnt.append(-1)
    else:
        cnt.append(0)

divide(0,0,n)
print(cnt.count(-1),cnt.count(0),cnt.count(1),sep='\n')