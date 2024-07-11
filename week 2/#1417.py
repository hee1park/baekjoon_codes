# 1417
i_n_candidates = int(input())

d_cand_votes = {}
for i in range(i_n_candidates):
    i_votes = int(input())
    d_cand_votes[i] = i_votes

max_votes_cand = i_n_candidates - 1
i_buy = 0

while True:
    # 최다 득표자 찾기
    for j in range(i_n_candidates):
        if d_cand_votes[max_votes_cand] <= d_cand_votes[j]:
            max_votes_cand = j
            
    # 최다 득표자가 다솜이면 멈춘다.
    if max_votes_cand == 0:
        break
    # 최다 득표자가 다솜이가 아니면 최다 득표자의 득표수 1을 다솜이에게 옮겨준다.
    else:
        d_cand_votes[max_votes_cand] -= 1
        d_cand_votes[0] += 1
        i_buy += 1

print(i_buy)
