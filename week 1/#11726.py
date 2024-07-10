# 11726
i_n = int(input())

# (2 * a) + (1 * b) = i_n
l_a = [i for i in range(i_n//2 + 1)]
l_ab = list(zip(l_a, map(lambda k : i_n - k * 2, l_a))) #가능한 가로, 세로 조합을 (a, b)로 표현
result = 0

#(a, b)에서 '같은 것이 있는 순열'로 경우의 수를 구함 : (a+b)!/a!b!
for x in l_ab:
    a, b = x
    fact_ab = 1
    for i in range(1, a+b+1):
        fact_ab *= i
    fact_a = 1
    for j in range(1, a+1):
        fact_a *= j
    fact_b = 1
    for k in range(1, b+1):
        fact_b *= k

    ways = fact_ab // (fact_a * fact_b)

    result += ways

print(result % 10007)


