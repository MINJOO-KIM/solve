def solution(tickets):
    
    tickets.sort(key=lambda x: (x[0],x[1]))
    print(tickets)
    
    def getPath(t, path):
        if len(t)==0:
            return path
        
        now = path[-1] # 바로 다음 경로
        valid_idx = -1
        
        # 출발지 현재 공항인거부터
        for i in range(len(t)):
            if t[i][0]==now:
                valid_idx = i
                break
        if valid_idx == -1:
            return []
        
        while t[valid_idx][0]==now:
            # 현재 탐색 장소를 제외한 남은 티켓 리스트, 기존 경로에 새로운 도착지를 더한 다음 경로
            next_path = getPath(t[:valid_idx]+t[valid_idx+1:], path+[t[valid_idx][1]])
            
            if next_path != []: # 성공
                return next_path
            
            valid_idx += 1 # 실패, 다음 장소 탐색
            
        return [] # 앞에서 return 못했다는건 실패

    return getPath(tickets, ["ICN"])