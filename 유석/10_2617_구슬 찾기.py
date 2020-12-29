import sys
sys.stdin = open("../../../test/bead.txt", "r")
read = sys.stdin.readline
N, M = map(int, read().rstrip().split())
heavy_graph = {}
light_graph = {}
for _ in range(M):
    h, l = map(int, read().rstrip().split())
    if h not in heavy_graph:
        heavy_graph[h] = []
    if l not in light_graph:
        light_graph[l] = []
    heavy_graph[h].append(l)
    light_graph[l].append(h)


def dfs(v, graph):
    stack = []
    count = 0
    stack.append((v, count))
    while stack:
        v, count = stack.pop()
        if v in graph:
            count += len(graph[v])
            if count > N // 2:
                return 1
            for w in graph[v]:
                stack.append((w, count))
    return 0

answer = 0
for i in range(1, N+1):
    answer += dfs(i, heavy_graph)
    answer += dfs(i, light_graph)

print(answer)