import sys
from collections import deque
sys.stdin = open("../../../test/tomato.txt", "r")
cube = list()
M, N, H = map(int, input().split())
# 큐브 생성
for _ in range(H):
    temp_list = list()
    for _ in range(N):
        temp_list.append(list(map(int, list(sys.stdin.readline().split()))))
    cube.append(temp_list)
# bfs 돌릴 때 상, 하, 좌, 우, 전, 후 움직이는 좌표
dx = [0, 0, 1, -1, 0, 0]
dy = [0, 0, 0, 0, 1, -1]
dz = [1, -1, 0, 0, 0, 0]
# (H, N, M) 순서임

# bfs 큐
dq = deque()


def bfs():
    count = 0
    count_0 = 0
    # 처음부터 1인 vertex들 좌표를 큐에 넣어줌
    for i in range(H):
        for j in range(N):
            for k in range(M):
                if cube[i][j][k] == 0:
                    count_0 += 1
                if cube[i][j][k] == 1:
                    dq.append((i, j, k))
    # 처음 1들 다 넣었으면 1을 큐에 넣어줌
    dq.append(1)
    # 전부 0이거나 전부 1 또는 -1이면 0 출력
    if count_0 == H*N*M or count_0 == 0:
        return 0
    while dq:
        # dq 제일 앞에 노드가 튜플이면 팝
        if dq[0] != 1:
            x, y, z = dq.popleft()
        # dq 제일 앞 노드가 1이면 하루가 지난 것이므로 팝해서 카운트에 더해준 뒤, 다시 1을 넣어줌.
        # 첫 익은 토마토가 다음 토마토를 익힌 후 1이 들어간다.
        # 2일 토마토가 3일 토마토를 익힌 후 1이 들어간다. ( 즉, 2일만 3일 토마토가에 익은건 큐에서데 마지막 1을 더하면 3일동안 익은 걸로 됨)
        # 즉, 마지막 하나 남은 1은 빼주면 안된다.
        else:
            if len(dq) != 1:
                count += dq.popleft()
                dq.append(1)
                continue
            else:
                break
        # 전형적인 BFS 탐색
        for i in range(6):
            next_x, next_y, next_z = x+dx[i], y+dy[i], z+dz[i]
            if 0 <= next_x < H and 0 <= next_y < N and 0 <= next_z < M:
                if cube[next_x][next_y][next_z] == 0:
                    cube[next_x][next_y][next_z] = 1
                    dq.append((next_x, next_y, next_z))
    # BFS가 끝났는데 0이 남아 있으면 익지 못하는 토마토니까 -1 출력
    for i in range(H):
        for j in range(N):
            for k in range(M):
                if cube[i][j][k] == 0:
                    return -1
    return count

print(bfs())