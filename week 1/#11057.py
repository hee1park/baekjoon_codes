# 11057
i_n = int(input())

# 끝자리가 0이면 0~9까지 10가지, 1이면 1~9까지 9가지, ..., 9이면 9 1가지의 한 자리 더 긴 오르막 수를 만들 수 있다.
# dictionary의 key들은 오르막수의 끝자리이고 value는 key로 끝나는 오르막수의 개수이다.
d_ascent = dict(zip(map(int, '0123456789'), [1]*10))
d_next_ascent = {}

for i in range(i_n - 1):
    d_next_ascent =  dict(zip(map(int, '0123456789'), [0]*10))
    for j in range(10):
        # '끝자리가 n인 오르막수'에서 다음 오르막수를 만들면 '끝자리가 range(n, 10)인 다음 오르막수'들의 개수가 '끝자리가 n인 오르막수'의 개수만큼 증가한다.
        for k in range(j, 10):
            d_next_ascent[k] += d_ascent[j]
    d_ascent = d_next_ascent

i_result = 0
for i in d_ascent.values():
    i_result += i

print(i_result % 10007)
    

    
##시간 초과##
##i_n = int(input())
##
##l_ascent = []
##for i in range(10):
##    l_ascent.append(str(i))
##
##while True:
##    if len(l_ascent[0]) < i_n:
##        s_num = l_ascent.pop(0)
##        for k in range(int(s_num[-1]), 10):
##            l_ascent.append(s_num + str(k))
##    else:
##        break
##
##print(len(l_ascent) % 10007)

