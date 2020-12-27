import sys
sys.stdin = open("input.txt", "r")

N, M = map(int, sys.stdin.readline().split())
arr = {i + 1: [] for i in range(N)}
order = [0] * (N + 1)

for _ in range(M):
    a, b = map(int, sys.stdin.readline().split())
    arr[a].append(b)
    order[b] += 1

queue = []
for i in range(N):
    if not order[i + 1]:
        queue.append(i + 1)  
answer = []

while queue:
    n = queue.pop()
    answer.append(n)
    for j in arr[n]:
        order[j] -= 1
        if order[j] == 0:
            queue.append(j)

print(*answer)