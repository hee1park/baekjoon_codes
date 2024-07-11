# 2870
i_N = int(input())

# 전체 숫자를 담을 리스트
l_i_number = []

for i in range(i_N):
    s_line = input()
    s_number = ''
    #한 줄에 대해
    for j in s_line:
        # 문자 j가 숫자인 경우 s_number에 j를 더해줌
        try:
            if type(int(j)) == int:
                s_number += j
        # 문자 j가 숫자가 아닌 경우 그 전까지 만들어진 s_number를 리스트에 넣어주고 s_number 초기화
        except:
            if s_number:
                l_i_number.append(int(s_number))
                s_number = ''
            else:
                continue
    # 한 줄에 대한 for문이 다 돌았는데 줄의 끝이 숫자인 경우
    if s_number:
        l_i_number.append(int(s_number))

l_sorted_num = sorted(l_i_number)

for k in l_sorted_num:
    print(k)

 
