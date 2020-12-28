import sys
sys.stdin = open("input.txt", "r")
input=sys.stdin.readline

n, m, v = map(int,input().split())
zone = [[0]*(n+1) for _ in range(n+1)]
for _ in range(m):
    line=list(map(int,input().split()))
    zone[line[0]][line[1]] = 1
    zone[line[1]][line[0]] = 1

def dfs(start, visited):
    visited += [start]
    for i in range(len(zone[start])):
        if zone[start][i] == 1 and i not in visited:
            dfs(i,visited)
    return visited

def bfs(start):
    visited=[start]
    que=[start]
    while que:
        n=que.pop(0)
        for i in range(len(zone[start])):
            if zone[n][i] == 1 and i not in visited:
                visited.append(i)
                que.append(i)
    return visited

print(*dfs(v,[]))
print(*bfs(v))
