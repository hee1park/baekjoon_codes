# 2559
i_n, i_k = map(int, input().split())
l_temp = list(map(int, input().split()))

i_cons = sum(l_temp[:i_k])
i_max = i_cons
for i in range(i_k, i_n):
    i_cons = i_cons - l_temp[i - i_k] + l_temp[i]
    # 이 부분을 sum()으로 매번 구하면 시간초과가 뜸
    # 프레임의 맨 앞 숫자는 빼고 그 뒤에 오는 숫자를 더하는 식으로 다음 합을 구함
    
    if i_cons > i_max:
        i_max = i_cons

print(i_max)
