import sys
input = sys.stdin.readline

n, m = map(int, input().split())
arr = list(map(int, input().split()))
pre_sum = [0]
cur_sum = 0

for i in range(n):
  cur_sum += arr[i]
  pre_sum.append(cur_sum)


for i in range(m):
  i, j = map(int, input().split())
  print(pre_sum[j] - pre_sum[i-1])