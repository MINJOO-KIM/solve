import sys
import heapq
input = sys.stdin.readline
n = int(input())
max_heap = []

for _ in range(n):
    num = int(input())

    if num> 0:
        heapq.heappush(max_heap, -num)

    else:
        if not max_heap:
            print(0)
        else:
            print(-heapq.heappop(max_heap))