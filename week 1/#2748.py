# 2748
i_n = int(input())

l_fibo = [1, 1]

if i_n == 1 or i_n == 2:
    print(1)

else:
    for i in range(2, i_n):
        l_fibo.append(l_fibo[i - 2] + l_fibo[i - 1])
    print(l_fibo[-1])
