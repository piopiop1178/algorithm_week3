import sys
sys.setrecursionlimit(1000000000)

N = int(sys.stdin.readline())
arr = {i:[] for i in range(1,N+1)}
for _ in range(N - 1):
    x, y = map(int, sys.stdin.readline().split())
    arr[x].append(y)
    arr[y].append(x)

parent = [0] * (N + 1)
def dfs(start):
    for i in arr[start]:
        if not parent[i]:
            parent[i] = start
            dfs(i)

dfs(1)
for i in range(2, len(parent)):
    print(parent[i])