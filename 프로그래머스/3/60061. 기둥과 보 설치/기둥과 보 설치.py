# 현재 설치된 구조물이 '가능한' 구조물인지 확인하는 함수
def possible(answer):
    for x,y,stuff in answer:
        # 기둥인 경우
        if stuff==0:
            if y==0 or [x-1,y,1] in answer or [x,y,1] in answer or [x,y-1,0] in answer: continue
            return False
        # 보인 경우
        elif stuff==1:
            if [x, y - 1, 0] in answer or [x + 1, y - 1, 0] in answer or ([x - 1, y, 1] in answer and [x + 1, y, 1] in answer):
                continue
            return False
    return True

def solution(n, build_frame):
    answer=[]
    for frame in build_frame:
        x,y,stuff,action = frame
        if action==0: # 삭제
            # 삭제해보고 가능한지 / 안되면 다시 복구
            answer.remove([x,y,stuff])
            if not possible(answer):
                answer.append([x,y,stuff])
        else: # 설치
            # 설치해보고 가능한지 / 가능하면 추가
            answer.append([x,y,stuff])
            if not possible(answer):
                answer.remove([x,y,stuff])
    return sorted(answer) 