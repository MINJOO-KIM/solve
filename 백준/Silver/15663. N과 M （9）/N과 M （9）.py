n,m = map(int, input().split())
arr = list(map(int, input().split()))
arr.sort()

path=['']*m
result = set()
used = [0]*n
def dfs(level):
    if level==m:
        # 리스트 path를 변경 불가능한 자료형인 튜플(tuple)로 바꿔서 넣기!
        result.add(tuple(path))
        return
    for i in range(n):
        if used[i]==1: continue
        path[level]=arr[i]
        used[i]=1
        dfs(level+1)
        used[i]=0
dfs(0)

for i in sorted(result):
    print(*i)
