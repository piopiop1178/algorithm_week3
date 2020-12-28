import sys
from collections import deque
sys.stdin = open('../../../test/line.txt', 'r')
read = sys.stdin.readline

N, M = map(int, read().rstrip().split())
graph = {}
indegree = [0 for _ in range(N+1)]

for i in range(1, N+1):
    graph[i] = []

for _ in range(M):
    A, B = map(int, read().rstrip().split())
    graph[A].append(B)
    indegree[B] += 1

dq = deque([i for i in range(1, N+1) if indegree[i] == 0])

def topology_sort():
    result = []
    while dq:
        now = dq.popleft()
        result.append(now)
        for v in graph[now]:
            indegree[v] -= 1
            if indegree[v] == 0:
                dq.append(v)
    print(*result)

topology_sort()