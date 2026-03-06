n = int(input())
for _ in range(n):
    dat1 = [0] * 26
    dat2 = [0] * 26
    first, second = map(str, input().split())
    for i in first:
        dat1[ord(i)-97]+=1
    for j in second:
        dat2[ord(j)-97] += 1
    flag = 1
    for i in range(26):
        if dat1[i]!=dat2[i]:
            flag=0
            break
    if flag:
        print("Possible")
    else:
        print("Impossible")