# 11057

i_n = int(input())

d_ascent = dict(zip(map(int, '0123456789'), [1]*10))
d_next_ascent = {}

for i in range(i_n - 1):
    d_next_ascent =  dict(zip(map(int, '0123456789'), [0]*10))
    for j in range(10):
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

