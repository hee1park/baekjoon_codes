### 1031
##
##def get_input(s):
##    ss = s.split("\n")
##    ss0 = [int(x) for x in ss[0].split()]
##    ss1 = [int(x) for x in ss[1].split()]
##    ss2 = [int(x) for x in ss[2].split()]
##
##    n = ss0[0]
##    m = ss0[1]
##
##    return n, m, ss1, ss2
##
##def make_table(n, m, ss1, ss2):
##    table = [[0] * m for _ in range(n)]
##    for i in ss1:
##        for k in range(i):
##            if 
##    
##    print(table)
##
##a = """3 3
##1 2 3
##3 1 2"""
##n, m, ss1, ss2 = get_input(a)
##make_table(n, m, ss1, ss2)


### 2920
##note_list = list(map(int, input().split()))
##
##result, prev = '', ''
##if note_list[0] < note_list[1]:
##    result = 'ascending'
##else:
##    result = 'descending'
##
##i = 1
##while i < len(note_list)- 1:
##    prev = result
##    if note_list[i] < note_list[i+1]:
##        result = 'ascending'
##    else:
##        result = 'descending'
##
##    if result != prev:
##        print('mixed')
##        break
##    else:
##        i += 1
##
##if i == len(note_list) - 1:
##    print(result)


### 2851
##
##total = 0
##
##for i in range(10):
##    i_n = int(input())
##
##    if (100 - total - i_n)**2 <= (100 - total)**2:
##        total += i_n
##    else:
##        break
##
##print(total)


# 1292

a, b = map(int, input().split())

i = 0
n = 1
i_list = []

while i < b:
    for j in range(n):
        i += 1
        i_list.append(n)
    n += 1

result = 0
for k in range(a-1, b):
    result += i_list[k]
    
print(result)
    

