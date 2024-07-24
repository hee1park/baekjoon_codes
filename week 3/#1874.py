# 1874
# stack으로 사용할 deque을 불러온다.
from collections import deque

i_n = int(input())

l_seq = []
for _ in range(i_n):
    l_seq.append(int(input()))

d_seq = deque()
num = 0
current_max = 0
s_push_pop = ''
b_possible = True

for i_a in l_seq:
    # 이번 항의 숫자가 이전까지 나왔던 항의 숫자들보다 크면 연속된 숫자 append
    if i_a > current_max:
        while num < i_a:
            num += 1
            d_seq.append(num)
            s_push_pop += '+'
        current_max = i_a
    # stack에서 pop을 했을 때 이번 항의 숫자가 안 나오면 'NO'
    if d_seq.pop() != i_a:
        print('NO')
        b_possible = False
        break
    s_push_pop += '-'
    
if b_possible:
    for i in s_push_pop:
        print(i)
