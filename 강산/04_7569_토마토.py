import sys
from collections import deque
sys.stdin = open("input.txt", "r")  

M, N, H = map(int, sys.stdin.readline().split())
tomato = [list(map(int, sys.stdin.readline().split())) for _ in range(N * H)]

def bfs(M, N, H, tomato):
    queue = deque([])
    check = [[0] * M for _ in range(N * H)]

    for x in range(M):
        for y in range(N * H):
            if tomato[y][x] == 1:
                queue.append((x, y))
                check[y][x] = 1

    dx = [1, -1, 0, 0]
    dy = [0, 0, 1, -1]

    while queue:
        x, y = queue.popleft()
        day = check[y][x]
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if  0 <= nx < M and 0 <= ny < N * H and ny // N == y // N:
                if not tomato[ny][nx] and not check[ny][nx]:
                    queue.append((nx, ny))
                    tomato[ny][nx] = 1
                    check[ny][nx] = day + 1

        if 0 <= y - N and not tomato[y - N][x] and not check[y - N][x]:
            queue.append((x, y - N))
            tomato[y - N][x] = 1
            check[y - N][x] = day + 1

        if y + N < N * H and not tomato[y + N][x] and not check[y + N][x]:
            queue.append((x, y + N))
            tomato[y + N][x] = 1
            check[y + N][x] = day + 1
        
    print(check)
    answer = 0
    for x in range(M):
        for y in range(N*H):
            if tomato[y][x] == 0:
                return -1
            answer = max(answer, check[y][x])

    return answer - 1

print(bfs(M, N, H, tomato))