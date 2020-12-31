import sys
sys.stdin = open("../../../test/bead.txt", "r")
read = sys.stdin.readline
N, M = map(int, read().rstrip().split())
heavy_graph = {i: [] for i in range(1, N+1)}
light_graph = {i: [] for i in range(1, N+1)}
for _ in range(M):
    h, l = map(int, read().rstrip().split())
    heavy_graph[h].append(l)
    light_graph[l].append(h)


def dfs(v, graph):
    repeat_list = [1 for _ in range(N + 1)]
    stack = []
    count = 0
    stack.append(v)
    while stack:
        v = stack.pop()
        for w in graph[v]:
            if repeat_list[w]:
                repeat_list[w] = 0
                count += 1
                if count > N//2:
                    return 1
                stack.append(w)
    return 0

answer = 0
for key in heavy_graph:
    answer += dfs(key, heavy_graph)
for key in light_graph:
    answer += dfs(key, light_graph)

print(answer)
