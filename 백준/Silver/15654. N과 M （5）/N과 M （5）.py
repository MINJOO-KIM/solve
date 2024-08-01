# 순열
n,m = map(int, input().split())
arr = sorted(list(map(int, input().split())))

path=['']*m
used=[0]*n
def dfs(level):
    if level==m:
        for i in range(level):
            print(path[i],end=' ')
        print()
        return

    for i in range(len(arr)):
        if used[i]==1: continue
        path[level]=arr[i]
        used[i]=1
        dfs(level+1)
        used[i]=0

dfs(0)