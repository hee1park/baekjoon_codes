# 17413
s_line = input()

l_word = []
s_word = ''

b_tag = False # 태그이면 True, 단어면 False

for i in s_line:
    if i == '<':
        l_word.append((b_tag, s_word)) # '<' 전까지는 단어
        b_tag = True
        s_word = ''
    
    s_word += i
    
    if i == '>':
        l_word.append((b_tag, s_word)) # '>' 전까지는 태그
        b_tag = False
        s_word = ''
        
if s_word:
    l_word.append((b_tag, s_word))
s_result = ''
for j in l_word:
    s_converted = ''
    if j[0] == False:  # 태그가 아닌 단어들이므로 뒤집어준다.
        for word in j[1].split():
            s_converted += word[::-1] + ' '
        s_converted = s_converted.strip()
    else:
        s_converted = j[1] # 태그는 그대로 둔다. 
    s_result += s_converted # 전체 문자열에 붙이기
    
print(s_result)
