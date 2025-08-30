import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

def dfs(n,result):
    visited[n]=True
    cycle.append(n)

    next = nums[n]
    # 방문했으면 사이클에 있는지 확인
    if  visited[next]:
        if next in cycle:
            # 연속적으로 cycle에 추가하기때문에
            result += cycle[cycle.index(next):]
    # 아직 방문안했으면 계속 탐색
    else:
        dfs(next,result)

for _ in range(int(input())):
    n = int(input())
    nums = [0]+list(map(int, input().split()))
    visited = [True]+[False]*n

    result = []
    for i in range(1,n+1):
        if not visited[i]:
            cycle = []
            dfs(i,result)

    print(n-len(result))