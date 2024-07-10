# 11655

s_line = input()
s_upper = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
s_lower = 'abcdefghijklmnopqrstuvwxyz'

s_rot13 = ''
for i in s_line:
    if i in s_upper:
        s_rot13 += s_upper[(s_upper.index(i) + 13) % 26]
    elif i in s_lower:
        s_rot13 += s_lower[(s_lower.index(i) + 13) % 26]
    else:
        s_rot13 += i

print(s_rot13)
        
        
