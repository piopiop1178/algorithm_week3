import sys
# sys.stdin = open("../../../test/find-parent.txt", "r")
sys.setrecursionlimit(10**5)
read = sys.stdin.readline

# 그래프 만들기
node_n = int(read())
graph = {}
for _ in range(node_n-1):
    k, v = map(int, read().rstrip().split())
    if k not in graph:
        graph[k] = []
    if v not in graph:
        graph[v] = []
    graph[k].append(v)
    graph[v].append(k)

# 그래프 value가 부모가 아니면 dfs하면서 리스트에 저장
parent_list = list(0 for _ in range(node_n))
def dfs(start_v, parent):
    parent_list[start_v-1] = parent
    for v in graph[start_v]:
        if v != parent:
            dfs(v, start_v)


dfs(1, 0)
for i in range(1, node_n):
    print(parent_list[i])