n,r,c = map(int, input().split())

def check(n,r,c):
    p0,p1 = 2**(n-1), 2**(n)
    if r<p0 and c<p0:
        position=0
    elif r<p0 and p0<=c<p1:
        position=1
    elif p0<=r<p1 and c<p0:
        position=2
    else:
        position=3

    return position

answer=0
while n>=1:
    now = 2**n * 2**n / (2*2)
    position = check(n,r,c)
    answer += now*position
    n-=1
    r,c = r % (2**n), c % (2**n)

print(int(answer))