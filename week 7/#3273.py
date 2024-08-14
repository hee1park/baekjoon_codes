# 3273
i_n = int(input())
l_i = list(map(int, input().split()))
i_x = int(input())

li_sorted = sorted(l_i)
i_count = 0
start = 0
end = i_n - 1

# 투 포인터 알고리즘
while start < end:
    i_sum = li_sorted[start] + li_sorted[end]
    if i_sum < i_x:
        start += 1
    elif i_sum > i_x:
        end -= 1
    else:
        i_count += 1
        start += 1
        end -= 1
        
print(i_count)
