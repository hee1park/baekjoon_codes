# 9625

i_k = int(input())

# (a 개수, b 개수)
# b 개수 = 이전 a 개수 + 이전 b 개수
# a 개수 = 이전 b 개수

d_ab = {0: (1, 0)}
for i in range(1, i_k + 1):
    d_ab[i] = (d_ab[i-1][1], d_ab[i-1][0] + d_ab[i-1][1])
    
print(*d_ab[i_k])
