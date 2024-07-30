# 순열

n,m = map(int, input().split())

# 순열로 만들 숫자들을 arr에 넣기
arr = []
for i in range(1,n+1):
    arr.append(i)
# 순열로 넣을 빈 배열 만들기
path = ['']*m
used = [0]*n

def dfs(level):

    if level==m:
        for i in range(level):
            print(path[i],end=' ')
        print()
        return

    for i in range(n):
        # level 돌 때마다, 숫자 채워주기
        path[level]=arr[i]
        # 순열이니까...
        used[i]=1
        dfs(level+1)
        used[i]=0
dfs(0)

