# 2164

# 덱 모듈을 이용해서 큐를 구현.
from collections import deque

i_n = int(input())

l_cards = [i for i in range(1, i_n + 1)]
d_cards = deque(l_cards)

while len(d_cards) > 1:
    d_cards.popleft()
    d_cards.append(d_cards.popleft())
print(d_cards.pop())
    
## 처음에는 리스트로 큐를 구현했으나 시간 초과 - deque 모듈이 가장 빨라 시간 안에 풀림
##while True:
##    l_cards.pop(0)
##    if len(l_cards) > 1:
##        l_cards.append(l_cards.pop(0))
##    else:
##        break  
##print(l_cards[0])


