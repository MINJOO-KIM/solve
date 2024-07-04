a = int(input())
b = int(input())
c = int(input())

ans = str(a*b*c)
DAT = [0]*10

for i in range(len(ans)):
    for j in range(10):
        if ans[i]==str(j):
            DAT[j]+=1

for i in range(len(DAT)):
    print(DAT[i])