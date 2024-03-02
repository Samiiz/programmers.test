def solution(common):
    lastNum = common[-1]
    if common[1] - common[0] == common[2] - common[1]:
        answer = lastNum + (common[1] - common[0])
    else :
        answer = lastNum * (common[1] / common[0])
    return answer