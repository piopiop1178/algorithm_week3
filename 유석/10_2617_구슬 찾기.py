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
    count = set()
    stack.append((v, count))
    while stack:
        v, count = stack.pop()
        if v in graph:
            for w in graph[v]:
                count.add(w)
                if len(count) > N//2:
                    return 1
                stack.append((w, count))
    return 0

answer = 0
for key in heavy_graph:
    answer += dfs(key, heavy_graph)
for key in light_graph:
    answer += dfs(key, light_graph)

print(answer)