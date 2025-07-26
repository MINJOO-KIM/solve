for _ in range(int(input())):
    p = [0]*101
    n = int(input())
    p[1]=1
    p[2]=1
    p[3]=1
    p[4]=2
    p[5]=2
    for i in range(6,n+1):
        p[i]=p[i-5]+p[i-1]
    print(p[n])