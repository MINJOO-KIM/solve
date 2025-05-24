N = int(input())
lst = []
for i in range(N):
    lst.append(int(input()))
lst.sort()

answer = []
for x in lst:
    answer.append(x*N)
    N-=1

print(max(answer))