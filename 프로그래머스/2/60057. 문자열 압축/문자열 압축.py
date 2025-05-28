def solution(s):
    
    # 1. 잘라서 배열에 넣기 (총 길이 절반까지 반복)
    # 2. 그 배열 돌면서 앞 문자랑 같으면 cnt랑 문자붙이기
    # 3. 총 길이 Min값에 갱신
    length = len(s)
    Min = 1001
    
    if length==1:
        return 1
    for n in range(1,length//2+1):
        cut = [s[i:i+n] for i in range(0, length, n)]
        res = ''
        
        cnt = 1
        cur = cut[0]
        
        for c in range(1,len(cut)):
            if cut[c]==cur:
                cnt+=1
            else:
                if cnt>1:
                    res+=str(cnt)+cur
                else:
                    res+=cur
                cnt=1
                cur=cut[c]
                
        if cnt>1:
            res+=str(cnt)+cur
        else:
            res+=cur
            
        Min=min(len(res), Min)
        
    return Min