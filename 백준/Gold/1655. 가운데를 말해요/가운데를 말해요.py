import heapq
import sys
input = sys.stdin.readline

n = int(input())
leftHeap = [] # 최대 힙
rightHeap = [] # 최소 힙
for _ in range(n):
    x=int(input())
    # left, right 길이 같으면 left에 삽입
    if len(leftHeap)==len(rightHeap):
        heapq.heappush(leftHeap,-x)
    else:
        heapq.heappush(rightHeap, x)
    # left는 중간값과 같거나 작은 값만 들어가게
    if leftHeap and rightHeap:
        if leftHeap[0]*(-1)>rightHeap[0]:
            left = heapq.heappop(leftHeap)
            right = heapq.heappop(rightHeap)

            heapq.heappush(rightHeap, -left)
            heapq.heappush(leftHeap, -right)
    print(leftHeap[0]*(-1))
