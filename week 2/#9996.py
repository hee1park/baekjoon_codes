# 9996
i_n = int(input())
s_pattern = input()
s_start, s_end = s_pattern.split('*')

l_result = []
# '*'의 앞, 뒤로 있는 문자열과 파일 이름의 앞에서부터 / 뒤에서부터가 일치하면 패턴 일치
# 단, aaa*abc 패턴에 파일명이 aaabc라면 s_start, s_end와는 일치하게 나오지만 'NE'가 나와야함
# 이를 구분하기 위해 파일 명이 패턴에서 '*'을 뺀 것보다 짧은 경우는 먼저 제외시킴
for i in range(i_n):
    s_file = input()
    if len(s_file) < len(s_pattern) - 1:
        l_result.append("NE")
    elif s_file[:len(s_start)] == s_start and s_file[-len(s_end):] == s_end:
        l_result.append("DA")
    else:
        l_result.append("NE")
        
for j in l_result:
    print(j)
