def solution(absolutes, signs):
    answer = 0
    for i, s in enumerate(absolutes):
        if not signs[i]:
            s = -s
        answer += s
        
    return answer
