import sys
from collections import deque
sys.stdin = open("input.txt", "r")  

N, M, V = map(int, sys.stdin.readline().split())

road = [[0] * (N + 1) for _ in range(N + 1)]

for _ in range(M):
    x, y = map(int, sys.stdin.readline().split())
    road[x][y] = 1
    road[y][x] = 1
print(road)

def dfs(road, start, answer):
    answer.append(start)
    for i in range(N + 1):
        if road[start][i] and i not in answer:
            answer = dfs(road, i, answer)
    return answer

def bfs(road, V):
    answer = [V]
    queue = deque([V])
    while queue:
        target = queue.popleft()
        for i in range(N + 1):
            if road[target][i] and i not in answer:
                queue.append(i)
                answer.append(i)
    return answer

print(*dfs(road, V, []))
print(*bfs(road, V))