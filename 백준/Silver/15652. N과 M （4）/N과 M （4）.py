n,m = map(int, input().split())
# n까지 m개씩
# 중복조합
ans=[]
path=['']*m

# ans에서 하나씩
for i in range(1,n+1):
    ans.append(i)

def dfs(level,start):
    if level==m:
        for i in range(level):
            print(path[i],end=' ')
        print()
        return

    # 중복조합이니까 ans에서 하나씩 뽑고 path에 넣으면 지나가
        # start 그대로
    for i in range(start,n):
        path[level]=ans[i]
        dfs(level+1,i)

dfs(0,0)