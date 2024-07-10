# 1463

# 재귀 사용 - 작동은 하지만 시간초과인 코드
##def cal(i_n):
##    if i_n == 1:
##        return 0
##
##    else:
##        
##        if i_n % 3 == 0:
##            d1 = cal(i_n // 3) + 1
##        else:
##            d1 = 10**7
##            
##        if i_n % 2 == 0:
##            d2 = cal(i_n // 2) + 1
##        else:
##            d2 = 10**7
##            
##        i_n -= 1
##        d3 = cal(i_n) + 1
##
##        return min(d1, d2, d3)
##
##i_n = int(input())
##print(cal(i_n))


#계속 틀리는 바람에 siwawa의 코드 참고함 - 경우별 min() 사용 아이디어 차용 
i_n = int(input())

d_shorts = {1: 0}
for i in range(2, i_n + 1):
    if i % 3 == 0 and i % 2 == 0:
        d_shorts[i] = min(d_shorts[i // 3], d_shorts[i // 2]) + 1
    elif i % 2 == 0:
        d_shorts[i] = min(d_shorts[i - 1], d_shorts[i // 2]) + 1
    elif i % 3 == 0:
        d_shorts[i] = min(d_shorts[i - 1], d_shorts[i // 3]) + 1
    else:
        d_shorts[i] = d_shorts[i - 1] + 1

print(d_shorts[i_n])

