# 11055
i_n = int(input())
li_a = list(map(int, input().split()))

# key : 현재 수열에서 가장 큰 숫자의 index
# vaule: 현재까지 수열의 합 list
d_sum = {0: li_a[0]}
# 현재 수열의 마지막 값(li_a[i])보다 작은 값들로 끝난 수열의 합 중의 최대에 li_a[i]를 더하면 이 값으로 끝나는 수열의 최대가 됨
for i in range(1, i_n):
    former_max = 0
    for j in range(i):
        if li_a[i] > li_a[j] and d_sum[j] > former_max: 
            former_max = d_sum[j]
    d_sum[i] = former_max + li_a[i]
    
print(max(d_sum.values()))
