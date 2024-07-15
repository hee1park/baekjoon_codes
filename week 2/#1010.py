i_t = int(input())

# 경우의 수는 mCn
# 1
# 11
# 121
# 1331
# 14641 ... 임을 활용
for _ in range(i_t):
    i_n, i_m = map(int, input().split())
    
    d_c = {(0, 0): 1}
    for a in range(1, i_m + 1):
        d_c[(a, 0)] = 1
        d_c[(a, a)] = 1
        for b in range(1, a):
           d_c[(a, b)] = d_c[(a-1, b-1)] + d_c[(a-1, b)]

    print(d_c[(i_m, i_n)])
    

# dp 사용하지 않은 풀이
# 바로 조합으로 계산
for _ in range(i_t):
    i_n, i_m = map(int, input().split())

    m_fact = 1
    for i in range(i_m):
        m_fact *= i + 1

    n_fact = 1
    for j in range(i_n):
        n_fact *= j + 1

    m_n_fact = 1
    for k in range(i_m - i_n):
        m_n_fact *= k + 1

    print(m_fact // (n_fact * m_n_fact))
        
