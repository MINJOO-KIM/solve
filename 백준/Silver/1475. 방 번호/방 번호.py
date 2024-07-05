num = input()
DAT = [0]*10

for i in range(len(num)):
    DAT[int(num[i])]+=1

maxOther,max69 = 0,0
ans=21e8

for i in range(len(DAT)):
    if i==6 or i==9: continue
    if DAT[i]>maxOther:
        maxOther=DAT[i]

if (DAT[6]+DAT[9])%2!=0:
    max69=(DAT[6]+DAT[9])//2+1
else:
    max69=(DAT[6]+DAT[9])//2

ans=max(maxOther,max69)
print(ans)