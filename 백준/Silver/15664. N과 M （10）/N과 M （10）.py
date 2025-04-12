n,m = map(int, input().split())
arr = list(map(int,input().split()))
path=['']*m
used= [0]*n
arr.sort()

result = set()

def dfs(level,start):
    if level==m:
        result.add(tuple(path))
        return
    for i in range(start,n):
        if used[i]==1: continue
        path[level]=arr[i]
        used[i]=1
        dfs(level+1, i+1)
        used[i]=0

dfs(0,0)
for i in sorted(result):
    print(*i)