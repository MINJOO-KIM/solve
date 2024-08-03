# 조합
n,m = map(int, input().split())
arr = sorted(list(map(int, input().split())))

path=['']*m
used=[0]*n
def dfs(level,start):
    if level==m:
        for i in range(level):
            print(path[i],end=' ')
        print()
        return

    for i in range(start,len(arr)):
        path[level]=arr[i]
        dfs(level+1,i+1)

dfs(0,0)