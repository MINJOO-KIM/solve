import sys
from collections import deque
input = sys.stdin.readline
tc = int(input())

for _ in range(1,tc+1):
    n = int(input())
    indegree = [0]*(n+1) # 진입차수 (들어오는 노드 개수)
    graph = [[False] * (n+1) for i in range(n+1)]

    # 작년 순위 정보
    data = list(map(int, input().split()))
    # 작년 순위 정보에 따라 간선 화살표 체크해주기 (a->b경로있으면 graph[a][b]가 True)
    for i in range(n):
        for j in range(i+1, n):
            graph[data[i]][data[j]]=True
            indegree[data[j]]+=1

    # 변경된 순위 정보
    m = int(input())
    for i in range(m):
        a,b = map(int, input().split())
        if graph[a][b]:
            graph[a][b] = False
            graph[b][a] = True
            indegree[a] += 1
            indegree[b] -= 1
        else:
            graph[a][b] = True
            graph[b][a] = False
            indegree[a] -= 1
            indegree[b] += 1

    result = [] # 알고리즘 수행 결과
    q = deque()

    # 진입차수 0인 노드부터 큐에 삽입
    for i in range(1,n+1):
        if indegree[i]==0:
            q.append(i)

    # 위상정렬 특이 케이스) 1. 위상정렬 결과가 여러개인 경우 2. 사이클이 발생하는 경우
    only_one = True
    cycle = False

    for i in range(n):
        # 사이클 발생 (큐가 비어있음)
        if len(q)==0:
            cycle = True
            break
        # 큐의 원소가 2개 이상이면 정렬 결과가 여러개
        if len(q)>=2:
            only_one = False
            break
        # 큐에서 원소 꺼내기
        now = q.popleft()
        result.append(now)
        # 해당 원소와 연결된 노드 진입차수 1 빼기
        for j in range(1,n+1):
            if graph[now][j]:
                indegree[j]-=1
                # 새롭게 진입차수가 0이 된 노드 큐에 삽입
                if indegree[j]==0:
                    q.append(j)

    if cycle:
        print("IMPOSSIBLE")
    elif not only_one:
        print("?")
    else:
        for i in result:
            print(i,end=" ")
        print()
