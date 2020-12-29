import sys
from collections import deque
sys.stdin = open("../../../test/toy.txt", "r")
read = sys.stdin.readline

N = int(read())
M = int(read())

graph = {}
indegree = [0 for _ in range(N+1)]
dq = deque([i for i in range(1, N+1) if indegree[i] == 0])

for _ in range(M):
    to_v, from_v, num = map(int, read().rstrip().split())
    if from_v not in graph:
        graph[from_v] = []
    graph[from_v].append((to_v, num))
    indegree[to_v] += 1

def topology_sort():
    result = []
    while dq:
        