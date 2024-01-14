def solution(n, arr1, arr2):
    answer = []
    translate = {0 : " ", 1 : "#"}
    for i in range(n):
        b = bin(arr1[i]|arr2[i])[2:].zfill(n)
        b = b.replace("0", " ").replace("1", "#")
        answer.append(b)
    print(answer)
    return answer
    