a, b = map(int, input().strip().split(' '))

answer = ""

for i in range(b):
    for j in range(a):
        answer += "*"
    print(answer)
    answer = ""
# a => 문자열(*) 갯수
# b => 행 갯수