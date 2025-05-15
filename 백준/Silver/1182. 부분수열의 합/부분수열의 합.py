def dfs(level,Sum, cnt):
    global ans
    # 종료 조건
    if level==N:
        if Sum==S and cnt>0:
            ans+=1
        return

    # 포함 o
    dfs(level+1, Sum+arr[level], cnt+1)
    # 포함 x
    dfs(level+1, Sum, cnt)

N, S = map(int, input().split())
arr = list(map(int, input().split()))
ans = 0
# level이 N일 때까지
    #  포함o / 포함x 두가지로 가지치기로 합 구하기
dfs(0,0,0)
print(ans)