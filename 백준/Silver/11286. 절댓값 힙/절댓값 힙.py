import sys
import heapq

input = sys.stdin.readline

n = int(input())
h = []

for _ in range(n):
    num = int(input())
    if num != 0:
        heapq.heappush(h, (abs(num),num))
    else:
        if h:
            # 절댓값이 가장 작은 기준으로 실제 값
            print(heapq.heappop(h)[1])
        else:
            print(0)
