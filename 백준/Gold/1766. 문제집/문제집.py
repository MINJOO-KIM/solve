import sys
import heapq
from collections import deque
input = sys.stdin.readline

n,m = map(int, input().split())
graph = [[] for i in range(n+1)]
indegree = [0]*(n+1)
heap = []

for _ in range(m):
    a,b = map(int, input().split())
    graph[a].append(b)
    indegree[b]+=1

def topology_sort():
    result = []

    for i in range(1,n+1):
        if indegree[i]==0:
            heapq.heappush(heap,i)
    while heap:
        now = heapq.heappop(heap)
        result.append(now)

        for i in graph[now]:
            indegree[i]-=1
            if indegree[i]==0:
                heapq.heappush(heap,i)
    for i in result:
        print(i,end=" ")

topology_sort()
