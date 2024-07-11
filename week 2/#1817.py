# 1817
# 짐 챙기는 숌

i_n, i_m = map(int, input().split())
i_boxes = 0

if i_n > 0:
    l_books_w = list(map(int, input().split()))

    i_box_w = 0
    for i in l_books_w:
        if i_box_w + i <= i_m:
            i_box_w += i
        else:
            i_boxes += 1
            i_box_w = i
            
    if i_box_w > 0:
        i_boxes += 1
        
print(i_boxes)
