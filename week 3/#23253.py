# 23253
# 어느 무더기에 있든지 상관 없이 번호가 더 낮은 책이 아래에 깔려 있으면 꽝임을 이용
import sys

def organize_books():
    i_n, i_m = map(int, input().split())
    l_book_pile = []
    for i in range(i_m):
        i_k_i = int(sys.stdin.readline())
        l_books = list(map(int, sys.stdin.readline().split()))
        l_book_pile.append((i_k_i, l_books))

    sorted_pile = sorted(l_book_pile, key = lambda x: x[0]) # 책이 적은 무더기부터 확인하기 위해 정렬
    for j in sorted_pile:
        if j[0] > 1:
            for x, y in zip(j[1][:-1], j[1][1:]):
                if x < y:
                    return 'No'
    return 'Yes'

print(organize_books())


