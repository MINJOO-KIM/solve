def solution(n, lost, reserve):
    
    lost.sort()
    reserve.sort()
    new_lost = []
    
    # 중복 제거
    for i in lost:
        if i in reserve:
            reserve.remove(i)
        else:
            new_lost.append(i)
            
    # 앞사람한테만 빌려주도록
    for i in reserve:
        if i-1 in new_lost:
            new_lost.remove(i-1)
        elif i+1 in new_lost:
            new_lost.remove(i+1)
            
    answer = n- len(new_lost)
    return answer