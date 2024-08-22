ts = int(input())
for t in range(1,ts+1):
    n = int(input())
    arr = list(map(int, input().split()))
    arr.reverse()
    Max = arr[0]
    Sum = 0

    for i in range(1,n):
        if arr[i]>Max:
            Max=arr[i]
        else:
            Sum+= Max-arr[i]
    print(Sum)