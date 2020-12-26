import sys
from collections import deque
sys.setrecursionlimit(10**5)
sys.stdin = open("../../../test/dfs-bfs.txt", "r")

N, M, V = map(int, input().split())

graph = {}
dq = deque()
discovered = []


for _ in range(M):
    k, v = map(int, sys.stdin.readline().split())
    if k not in graph:
        graph[k] = []
    if v not in graph:
        graph[v] = []
    graph[k].append(v)
    graph[v].append(k)


# # 재귀로 구현 1
# def dfs(start_v):
#     discovered.append(start_v)
#     if start_v in graph and graph[start_v]:
#         graph[start_v].sort()
#         for i in graph[start_v]:
#             if i not in discovered:
#                 dfs(i)
# dfs(V)
# print(*discovered)

# 재귀로 구현 2
def dfs_1(v, dis):
    dis.append(v)
    if v in graph:
        graph[v].sort()
        for w in graph[v]:
            if w not in dis:
                dis = dfs_1(w, dis)
    return dis


print(*dfs_1(V, discovered))


# 스택으로 구현
# def dfs_2(start_v):
#     stack = [start_v]
#     discovered = []
#     while stack:
#         v = stack.pop()
#         if v not in discovered:
#             discovered.append(v)
#             if v in graph:
#                 graph[v].sort(reverse=True)
#                 for w in graph[v]:
#                     stack.append(w)
#     return discovered
#
#
# print(*dfs_2(V))


# 큐로 구현
def bfs(start_v):
    found = [start_v]
    dq.append(start_v)
    while dq:
        v = dq.popleft()
        if v in graph:
            graph[v].sort()
            for w in graph[v]:
                if w not in found:
                    found.append(w)
                    dq.append(w)
    return found


print(*bfs(V))