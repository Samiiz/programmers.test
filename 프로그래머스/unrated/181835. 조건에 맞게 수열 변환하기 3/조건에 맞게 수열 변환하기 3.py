def solution(arr, k):
    
    answer = []
    
    if k % 2 == 1:  # k가 홀수인 경우
        answer = [num * k for num in arr]
    else:  # k가 짝수인 경우
        answer = [num + k for num in arr]
        
    return answer