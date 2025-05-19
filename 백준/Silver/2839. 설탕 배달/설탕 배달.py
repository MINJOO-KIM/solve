n=int(input())
ans = 0

# 5로 나눠떨어지면, 5를 우선적으로 사용 (더 큰 봉지 사용)
while n>=0:
    if n%5==0:
        ans+=n//5
        print(ans)
        break
    n-=3
    ans+=1
else:
    print(-1)