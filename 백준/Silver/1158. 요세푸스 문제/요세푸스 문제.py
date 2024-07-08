from collections import deque
n, k = map(int, input().split())

q = deque()
ans = []

for i in range(n):
    q.append(i+1)
# q = deque(range(1,n+1))

while q:
    for _ in range(k-1):
        # k를 범위로, q의 왼쪽값을 popleft로 빼서 제거할 k번째 수를 제일 왼쪽에 두기
        q.append(q.popleft())
    ans.append(q.popleft())

# 혹은 나머지 활용하기
# for t in range(N):
#     num += K - 1
#     if num >= len(arr):  # 한바퀴를 돌고 그다음으로 돌아올때를 대비해 값을 나머지로 바꿈
#         num = num % len(arr)
#
#     answer.append(str(arr.pop(num)))

# [를 <로 교체하기
print(str(ans).replace('[','<').replace(']','>'))
# print("<{}>".format(', '.join(ans)))
# print("<",", ".join(ans)[:],">", sep='')