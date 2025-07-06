# a -> b 까지 가는 최소 비용 : 우선순위 큐 이용한 다익스트라
import sys
import heapq

input = sys.stdin.readline
n = int(input())
m = int(input())
INF = int(1e9)

graph = [[] for _ in range(n+1)]
distance = [INF]*(n+1)
# visited = [False]*(n+1)

# 간선 정보 입력
for _ in range(m):
    a,b,c = map(int, input().split())
    graph[a].append((b,c)) # (도시,비용)

start,end = map(int, input().split())


def dijkstra(start):
    # 시작 노드 초기화
    q = []
    heapq.heappush(q, (start, 0))
    distance[start] = 0

    # 가능한 경로 탐색
    while q:
        now,dist = heapq.heappop(q)
        # 방문 여부
        if distance[now]<dist:
            continue
        # 경로 탐색
        for i in graph[now]: #i[0]:도시, i[1]:비용
            cost = dist + i[1]
            if cost < distance[i[0]]:
                distance[i[0]] = cost
                heapq.heappush(q,(i[0],cost))

dijkstra(start)
print(distance[end])
