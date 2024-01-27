def solution(s, n):
    answer = ''
    
    for i in s:
        if i.isalpha():
            start = ord('a') if i.islower() else ord('A')
            change = chr((ord(i) - start + n)%26 + start)
            
            answer += change
        else :
            answer += i
        
    return answer

# (i - 65 또는 97의 아스키코드 + n) % 26 + 65, 97
# z, Z (90, 122) 를 넘어가면 a, A (65, 97)로 시작해야함
## 수학 어려워 이건 파이썬 잘하냐가 아니라 수학문제 잖아 ㅠㅠㅠㅠ