def solution(number):
    answer = 0

    for a in range(len(number)):
        for b in range(a+1, len(number)):
            for c in range(b+1, len(number)):
                    if number[a] + number[b] + number[c] == 0:
                        answer += 1
                        print(a, b, c)
    
    
    # for a in number:
    #     i = number.index(a)
    #     i = i + 1
    #     for b in number[i:]:
    #         q = number.index(b)
    #         q = q + 1
    #         for c in number[q:]:
    #             if a + b + c == 0
    #                 answer += 1
    #                 print(a, b, c)

    return answer


