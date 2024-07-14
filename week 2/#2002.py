# 2002
i_n = int(input())

l_in= []
l_out = []

for i1 in range(i_n):
    l_in.append(input())

for i2 in range(i_n):
    l_out.append(input())

j, k = 0, 0
passing_count = 0
l_passing = []

while j < (i_n - 1) and k <= (i_n - 1):
    if l_in[j] == l_out[k]:
        j += 1
        k += 1
    elif l_in[j] not in l_passing:
        l_passing.append(l_out[k])
        passing_count += 1
        k += 1
    else:
        j += 1

print(passing_count)

