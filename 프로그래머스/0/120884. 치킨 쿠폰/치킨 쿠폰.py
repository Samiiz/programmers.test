def solution(chicken):
    cupon = chicken
    service = 0
    for i in range(chicken):
        if cupon >= 10:
            service += cupon // 10 # 서비스 108개
            cupon = cupon % 10 + cupon // 10
            # if cupon >= 10:
            #     service += service // 10
    return service
            
    
    
    return service
            