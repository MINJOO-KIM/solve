n,k = map(int, input().split())
up=1
down=1
for i in range(1,k+1):
    up*=n
    n-=1
    down*=i
print(up//down)