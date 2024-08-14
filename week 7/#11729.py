# 11729

n = int(input())
# (출발, 도착) 막대 저장 리스트
l_move = []
# 세 막대를 표현한 딕셔너리
d_tower = {1: ['disc'] * n, 2: [], 3: []}

def hanoi(n, i_from, i_middle, i_to): # (n, 시작, 중간, 목적지) 순서
    if n == 1:
        # 원반이 하나이면 시작 막대에서 목적지 막대로 옮겨줌
        d_tower[i_to].append(d_tower[i_from].pop())
        l_move.append((i_from, i_to))
        
    else:
        # 원반이 하나 이상이면 가장 아래 원반을 제외하고 중간 막대로 옮겨줌
        hanoi(n-1, i_from, i_to, i_middle)

        # 가장 아래 원반은 목적지 막대로 옮겨줌
        d_tower[i_to].append(d_tower[i_from].pop())
        l_move.append((i_from, i_to))

        # 나머지 원반도 목적지 막대로 옮겨줌
        hanoi(n-1, i_middle, i_from, i_to)

hanoi(n, 1, 2, 3)

print(len(l_move))
for i in l_move:
    print(*i)      
