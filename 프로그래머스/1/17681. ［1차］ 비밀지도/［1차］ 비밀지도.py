def solution(n, arr1, arr2):
    # for문으로 도출된 값을 전부 추가하기 위해 answer라는 빈배열을 만든다
    answer = []
    # n열만큼 반복하는 반복문을 만든다.
    for i in range(n):
        # bin(10진수) => "ob2진수"
        # 숫자열1 | 숫자열2 => 숫자열1(2진수) or 숫자열2(2진수)
        # zfill(n) => n자릿수 만큼 해당 문자열의 왼쪽기준으로 빈자리를 0으로 채워준다.
        b = bin(arr1[i]|arr2[i])[2:].zfill(n)
        # b의 값을 기준으로 0 => " "(공백)으로, 1 => "#"으로 치환한다.
        b = b.replace("0", " ").replace("1", "#")
        # b에 할당한 값을 answer배열에 추가한다.
        answer.append(b)
    print(answer)
    return answer