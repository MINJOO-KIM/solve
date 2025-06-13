def solution(N, stages):
    answer = []
    
    fail = [0] * (N+2)
    face = [0] * (N+2)
    rate=[[0,0] for _ in range (N+2)]
    
    for i in range(len(stages)):
        fail[stages[i]]+=1
        
    cnt=fail[N+1]
    for i in range(N,0,-1):
        cnt+=fail[i]
        face[i]=cnt
    
    for i in range(1,N+1):
        rate[i][0]=i
        if face[i]==0:
            rate[i][1]=0
        else:
            rate[i][1]=(fail[i]/face[i])
        
    rate.sort(key=lambda x: (-x[1],x[0]))
    
    for i in range(len(rate)):
        if rate[i][0]!=0:
            answer.append(rate[i][0])
    
    return answer