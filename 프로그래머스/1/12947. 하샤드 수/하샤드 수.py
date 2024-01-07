def solution(x):
    answer = True
    
    X = str(x)
    a = 0
    for i in range(len(X)):
        a += int(X[i])
    if x % a != 0:
        answer = False
    
    return answer