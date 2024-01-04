def solution(num_list):
    answer = []
    
    last_num = num_list[-1]
    before_last_num = num_list[-2]
    
    if(last_num > before_last_num) :
        answer = num_list + [last_num - before_last_num]
    else :
        answer = num_list + [last_num * 2]
    
    return answer