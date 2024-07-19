# 27160
i_n = int(input())

d_fruit = {}
for _ in range(i_n):
    s_fruit, s_num = input().split()
    if s_fruit in d_fruit:
        d_fruit[s_fruit] += int(s_num)
    else:
        d_fruit[s_fruit] = int(s_num)

b_bell = False
for i in d_fruit.values():
    if i == 5:
        b_bell = True
        break

if b_bell:
    print('YES')
else:
    print('NO')
