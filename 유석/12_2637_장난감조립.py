import sys
from collections import deque
sys.stdin = open("../../../test/toy.txt", "r")
read = sys.stdin.readline

N = int(read())
M = int(read())

graph = {i: [] for i in range(1, N+1)}
indegree = [0 for _ in range(N+1)]

for _ in range(M):
    from_v, to_v, num = map(int, read().rstrip().split())
    graph[from_v].append((to_v, num))
    indegree[to_v] += 1
dq = deque([N])

save = [0 for _ in range(N+1)]
answer = []


def topology_sort():
    while dq:
        v = dq.popleft()
        if graph[v]:
            for value in graph[v]:
                w, mul = value
                if save[v]:
                    save[w] += save[v]*mul
                else:
                    save[w] += mul
                indegree[w] -= 1
                if not indegree[w]:
                    dq.append(w)
        else:
            answer.append((v, save[v]))

topology_sort()
answer.sort()
for ans in answer:
    print(*ans)