# 9996

i_n = int(input())
s_pattern = input()
s_start, s_end = s_pattern.split('*')

l_result = []
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
