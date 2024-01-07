def solution(x):
    answer = True

#    for i in range(len(X)):
#        a += int(X[i])
    if x % sum(int(i) for i in str(x)) != 0:
        answer = False
    
    return answer