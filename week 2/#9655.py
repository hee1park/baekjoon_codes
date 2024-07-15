# 9655

i_n = int(input())
# 0: 시작한 사람이 짐
# 1: 시작한 사람이 이김
# keys => 돌의 숫자
d_winner = {1: 1, 2: 0, 3: 1}
if i_n > 3:
    for i in range(4, i_n + 1):
        d_winner[i] = (d_winner[i-3] + 1) % 2

if d_winner[i_n] == 1:
    print('SK')
else:
    print('CY')

# 짜치는(?) 풀이
x = int(input()) % 2
if x == 1:
    print('SK')
else:
    print('CY')
