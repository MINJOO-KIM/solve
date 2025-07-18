n = int(input())
m = int(input())
graph = [[] for _ in range(n+1)]
visited = [False]*(n+1)

for _ in range(m):
    a,b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

cnt=0
def dfs(now):
    global cnt
    visited[now]=True
    for i in graph[now] :
        if not visited[i]:
            cnt+=1
            dfs(i)
dfs(1)
print(cnt)