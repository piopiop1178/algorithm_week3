import sys
from collections import deque
sys.stdin = open("../../../test/coin2.txt", "r")
n, k = map(int, sys.stdin.readline().split())
coin_list = list(int(sys.stdin.readline()) for _ in range(n))
bfs_que = deque()
overlap = {}

# bfs
def min_coins(head):
    count = 1
    bfs_que.clear()
    # 큐에 시작 vertex 넣어줌
    bfs_que.append((head, head))
    # 한 턴의 끝 표시
    bfs_que.append((-1, count))
    while bfs_que:
        v = bfs_que.popleft()
        if v[0] in coin_list:       # 큐에서 뽑은게 동전이면
            for w in coin_list:     # 각 동전들을 더해줌
                if v[1]+w not in overlap:
                    overlap[v[1]+w] = count
                elif overlap[v[1]+w] > count:
                    overlap[v[1]+w] = count
                else: continue
                if v[1] + w == k:       # 합이 원하는 값이면 리턴
                    return count+1      # 카운트는 턴이 끝나면 오르기 때문에 1을 높여서 리턴
                elif v[1] + w < k:
                    bfs_que.append((w, v[1]+w))      # 아니면 큐에 더해준다.
        else:
            if len(bfs_que) == 0: return 0      # 다 돌았는데 일치하는 값이 없으니 0 리턴return 0
            else:
                count += 1            # 아니면 한 턴이 끝났으니 카운트 +1
                bfs_que.append((-1, count))  # 한 턴이 끝났음을 표시


min_list = []
for head in coin_list:
    temp = min_coins(head)
    if temp != 0:
        min_list.append(temp)
if not min_list:
    print(-1)
else: print(min(min_list))

# 시작부터 bfs로 리팩토링 해야함