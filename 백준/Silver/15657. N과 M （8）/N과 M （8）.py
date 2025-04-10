n,m = map(int, input().split())
arr = list(map(int,input().split()))
arr.sort()
path = ['']*m

def dfs(level,start):
    if level==m:
        for i in range(level):
            print(path[i],end=" ")
        print()
        return
    for i in range(start,n):
        path[level]=arr[i]
        dfs(level+1,i)

dfs(0,0)