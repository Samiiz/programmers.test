a, b = map(int, input().strip().split(' '))

if a <= 100000 and b <= 100000 :
    a__str = (f"a = {a}")
    b__str = (f"b = {b}")
else :
    print("error")
print(a__str)
print(b__str)