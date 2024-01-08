def solution(x):
    answer = True # answer의 기본값을 True로 할당한다.
    
    X = str(x) # 입력값을 문자열 형태로 받기 위해 형변환 후 X라는 변수에 할당
    a = 0 # 나눈 수들의 합을 구하기 위해 a라는 변수에 0을 할당
    for i in range(len(X)):  # X의 길이("12"라면 2)만큼 for문의 반복 횟수를 정해준다.
        a += int(X[i]) # 문자열로 변경된 X의 i번째 인덱스값들을 정수로 변환한 후 a에 더한다.   -> 반복
    if x % a != 0: # 입력값 x를 a로 나눈 나머지가 0이 아닐시 라는 조건을 만든다.
        answer = False # answer에 False를 할당해서 입력값이 하샤드수가 아닐 시 False를 반환 하게 한다.
    
    return answer # 마지막으로 True or False가 할당된 answer을 반환한다