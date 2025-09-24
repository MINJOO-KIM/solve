import heapq
import sys
input = sys.stdin.readline
n = int(input())
heap = []
for _ in range(n):
    x = int(input())
    if x==0:
        if heap:
            # 절댓값이 같은게 여러개일때 가장 작은 수 출력
            print(heapq.heappop(heap)[1])
        else:
            print(0)
    else:
        # 튜플 (a, b) -> a값을 먼저 비교하고 b값을 비교
        heapq.heappush(heap,(abs(x),x))
