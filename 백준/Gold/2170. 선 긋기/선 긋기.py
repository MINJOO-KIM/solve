import sys
input = sys.stdin.readline
n = int(input())
lines = [tuple(map(int, input().split())) for _ in range(n)]
lines.sort()  # 시작점을 기준으로 정렬!

answer = 0
start, end = lines[0]

for x, y in lines[1:]:
    if x <= end:  # 겹침
        end = max(end, y)
    else:
        answer += end - start
        start, end = x, y

answer += end - start  # 마지막 구간 처리

print(answer)