def solution(chicken):
    cupon = chicken
    service = 0
    for i in range(chicken):
        if cupon >= 10:
            service += cupon // 10 # 서비스 108개
            cupon = cupon % 10 + cupon // 10 # 남은 쿠폰 1개 + 서비스 쿠폰 108개 = 109
    return service