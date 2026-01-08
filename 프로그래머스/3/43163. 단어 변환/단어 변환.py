from collections import deque
def solution(begin, target, words):  
    
    if target not in words:
        return 0
    
    answer = 0
    
    q = deque()
    q.append((begin,0))
    visited = [False]*len(words)
    
    while q:
        now, cnt = q.popleft()
        
        if now==target:
            return cnt
        
        for i in range(len(words)):
            if visited[i]==True:
                continue
                
            word = words[i]
            dif = 0
            for j in range(len(now)):
                if word[j]!=now[j]:
                    dif += 1
                    
            if dif==1:
                visited[i]=True
                q.append((word, cnt+1))
            
    return answer