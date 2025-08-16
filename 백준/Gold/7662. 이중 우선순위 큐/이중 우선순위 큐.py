import heapq
import sys
input = sys.stdin.readline

for _ in range(int(input())):
    n = int(input())
    visited = [False]*n
    min_heap = []
    max_heap = []

    for i in range(n):
        opr,num = input().split()
        num = int(num)

        if opr=='I':
            # 큐에 삽입
            # 동기화를 위해서 i 인덱스 함께 사용
            heapq.heappush(min_heap,(num,i))
            heapq.heappush(max_heap,(-num,i))
            visited[i]=True # True면 아직 삭제 되지 않은 상태 (존재중)

        elif opr=='D':
            if num == 1:
                # 큐에서 최댓값 삭제
                while max_heap and not visited[max_heap[0][1]]: # 일단 상대 힙에 의해 삭제된 노드 쭉 처리
                    heapq.heappop(max_heap)
                if max_heap:
                    visited[max_heap[0][1]]=False # 삭제 처리
                    heapq.heappop(max_heap)
            elif num == -1:
                # 큐에서 최솟값 삭제
                while min_heap and not visited[min_heap[0][1]]:
                    heapq.heappop(min_heap)
                if min_heap:
                    visited[min_heap[0][1]]=False
                    heapq.heappop(min_heap)

            elif num==-1:
                # 큐에서 최솟값 삭제
                heapq.heappop(min_heap)

    # 한 번씩 더 비우기 체크
    while max_heap and not visited[max_heap[0][1]]:
        heapq.heappop(max_heap)
    while min_heap and not visited[min_heap[0][1]]:
        heapq.heappop(min_heap)

    if min_heap and max_heap:
        print(-max_heap[0][0],min_heap[0][0])
    else:
        print('EMPTY')