# 4779

def cantor(n):
    if n == 0:
        return '-'
    else:
        return cantor(n - 1) + ' ' * 3**(n - 1) + cantor(n - 1)

while True:
    try:
        n = int(input())
        print(cantor(n))
    except:
        break
    
# (입력 방식이 다른 문제들이랑 달라서 화가 나는 문제였다....)
