import heapq
tc = int(input())
for t in range(1,tc+1):
    n = int(input())
    arr = list(map(int, input().split()))
    heapq.heapify(arr)
    ans=0
    # 정렬된 맨앞에 있는 두개를 빼고, 그 합을 넣어

    while len(arr)>1:
        temp=0
        a=heapq.heappop(arr)
        b=heapq.heappop(arr)
        temp += a+b
        ans += temp
        heapq.heappush(arr,temp)
    print(ans)