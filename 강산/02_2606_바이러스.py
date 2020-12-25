import sys
from collections import deque

N = int(sys.stdin.readline())
M = int(sys.stdin.readline())

graph = [[0] * (N + 1) for _ in range(N + 1)]
for _ in range(M):
    x, y = map(int, sys.stdin.readline().split())
    graph[x][y] = graph[y][x] = 1

def bfs(graph, start):
    answer =  0
    queue = deque([start])
    check = [0] * (N + 1)
    check[start] = 1
    while queue:
        node = queue.popleft()
        for i in range(N + 1):
            if graph[node][i] and not check[i]:
                queue.append(i)
                check[i] = 1
                answer += 1
    return answer

print(bfs(graph, 1))