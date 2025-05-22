S = input()
ans = S[0]

for i in range(len(S)-1):
    if S[i]=='0':
        if S[i+1]=='1':
            ans+='1'
    else:
        if S[i+1]=='0':
            ans+='0'

zero,one= 0,0
for i in ans:
    if i=='0':
        zero+=1
    elif i=='1':
        one+=1

if zero+one==1:
    print(0)
else:
    print(min(zero,one))