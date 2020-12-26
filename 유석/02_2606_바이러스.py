import sys
sys.stdin = open("../../../test/virus.txt", "r")

computer_n = int(input())
connect_n = int(input())
graph = {}


for _ in range(connect_n):
    v1, v2 = map(int, sys.stdin.readline().split())
    if v1 not in graph:
        graph[v1] = []
    if v2 not in graph:
        graph[v2] = []
    graph[v1].append(v2)
    graph[v2].append(v1)

infected = []


def dfs(v: int, dis: list) -> list:
    for w in graph[v]:
        if w not in dis:
            dis.append(v)
            dfs(w, dis)
    return dis


print(len(dfs(1, infected))-1)