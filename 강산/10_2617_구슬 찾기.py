import sys

sys.stdin = open("input.txt", "r")
N, M = map(int, sys.stdin.readline().split())
graph = [[0] * N for _ in range(N)]

for _ in range(M):
    a, b = map(int, sys.stdin.readline().split())
    graph[a - 1][b - 1] = 1
    graph[b - 1][a - 1] = -1

answer = 0

def dfs(i):
    global answer
    light_queue = []
    heavy_queue = []
    light_cnt = 0
    heavy_cnt = 0
    for j in range(N):
        if graph[i][j] == 1:
            heavy_queue.append(j)
            heavy_cnt += 1
        if graph[i][j] == -1:
            light_queue.append(j)
            light_cnt += 1
        if light_cnt > N // 2 or heavy_cnt > N // 2:
            answer += 1
            return 

    while light_queue:
        t = light_queue.pop()
        for k in range(N):
            if graph[t][k] == -1 and not graph[i][k]:
                light_queue.append(k)
                graph[i][k] = -1
                light_cnt += 1
            if light_cnt > N // 2:
                answer += 1
                return 
    
    while heavy_queue:
        t = heavy_queue.pop()
        for k in range(N):
            if graph[t][k] == 1 and not graph[i][k]:
                heavy_queue.append(k)
                graph[i][k] = 1
                heavy_cnt += 1
            if heavy_cnt > N // 2:
                answer += 1
                return

for i in range(N):
    dfs(i)            

print(answer)