def solution(triangle):
    answer = 0
    n = len(triangle)
    for i in range(1,n):
        for j in range(i+1):
            if j==0:
                up_left = 0
            else:
                up_left = triangle[i-1][j-1]
            if j==i:
                up = 0
            else:
                up = triangle[i-1][j]
                
            triangle[i][j]=triangle[i][j]+max(up_left,up)
    answer = max(triangle[n-1])        
    return answer