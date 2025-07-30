import sys
input = sys.stdin.readline
K, N = map(int, input().split())
lan = [int(input()) for _ in range(K)]
start, end = 1, max(lan)

while start <= end:  # 이분탐색
    mid = (start + end) // 2
    lines = 0  # 랜선 수
    for i in lan:
        lines += i // mid  # 분할된 랜선 수
    if lines >= N:
        start = mid + 1
    else:
        end = mid - 1

print(end)