import sys
sys.stdin = open("input.txt", "r")
input=sys.stdin.readline
sys.setrecursionlimit(10 ** 9)

n=int(input())
zones=[[] for _ in range(n+1)]
for _ in range(n-1):
    a, b=map(int, input().split())
    zones[a].append(b)
    zones[b].append(a)

parents=[0 for _ in range(n+1)]
parents[1]=1

def dfs(start, zone, parent):
    for i in zone[start]:
        if parent[i]==0:
            parent[i]=start
            dfs(i, zone, parent)

dfs(1, zones, parents)
for i in range(2, n+1):
    print(parents[i])


'''
def dfs(zone, start, parent):
    stack = [start]
    
    while stack:
        node = stack.pop()
        for i in zone[node]:
            parent[i].append(node)
            stack.append(i)
            zone[i].remove(node)
    return parent

for i in list(dfs(zones, 1, parents))[2:]:
    print(i[0])
'''