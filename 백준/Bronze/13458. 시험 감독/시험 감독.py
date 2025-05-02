N = int(input())
lst = list(map(int, input().split()))
B, C = map(int, input().split())

ans = N
# 총 감독관은 시험장 개수만큼 (1명씩 들어가니까)
# 총 감독관 -> 부 감독관
for n in lst:
    if n-B>0:
        ans+=(n-B + C-1)//C
print(ans)