# 1213
name = input()
d_letters = {}

for i in name:
    if i in d_letters:
        d_letters[i] += 1
    else:
        d_letters[i] = 1

l_letters = list(d_letters.keys())
l_sorted_letters = sorted(l_letters)

odds = 0
for j in d_letters:
    if d_letters[j] % 2 == 1:
        odds += 1
        odd = j

palindrome = ''
l_save = []

if odds > 1:
    print("I'm Sorry Hansoo")
else:
    for k in l_sorted_letters:
            for _ in range(d_letters[k] // 2):
                palindrome += k 
                l_save.append(k)
    if odds == 1:
        palindrome += odd
    for l in range(len(l_save)):
        palindrome += l_save.pop()
    print(palindrome)






    
