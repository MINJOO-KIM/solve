n = int(input())
s = [0]*301
d = [[0]*3 for _ in range(301)]
for i in range(1,n+1):
    s[i]=int(input())

d[1][1]=s[1]
d[1][2]=0

d[2][1]=s[2]
d[2][2]=s[1]+s[2]
for i in range(3,n+1):
    d[i][1]=max(d[i-2][1],d[i-2][2])+s[i]
    d[i][2]=d[i-1][1]+s[i]

print(max(d[n][1],d[n][2]))