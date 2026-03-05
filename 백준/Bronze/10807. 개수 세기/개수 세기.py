n = int(input())
num = list(map(int,input().split()))
v = int(input())
dat = [0]*201

for i in num:
    dat[i+100]+=1
print(dat[v+100])