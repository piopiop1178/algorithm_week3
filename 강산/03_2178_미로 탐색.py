import sys
from collections import deque

N, M = map(int, sys.stdin.readline().split())
graph = [list(map(int, list(sys.stdin.readline().rstrip()))) for _ in range(N)]

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

def bfs(graph, start):
    queue = deque([start])
    check = [[0] * M for _ in range(N)]
    check[0][0] = 1

    while queue:
        x, y, num = queue.popleft()
        if x == M - 1 and y == N - 1:
            break

        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if nx >= 0 and ny >= 0 and nx < M and ny < N and graph[ny][nx] and not check[ny][nx]:
                queue.append((nx, ny, num + 1))
                check[ny][nx] = 1
    return num

print(bfs(graph, (0, 0, 1)))