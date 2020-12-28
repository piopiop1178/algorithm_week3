import sys
sys.stdin = open("input.txt", "r")
input=sys.stdin.readline

c = int(input())
n = int(input())
zone = [[0]*(c+1) for _ in range(c+1)]
for _ in range(n):
    line = list(map(int, input().split()))
    zone[line[0]][line[1]]=zone[line[1]][line[0]] =1

def dfs(start,visited):
    visited+=[start]
    for i in range(len(zone[start])):
        if zone[start][i] == 1 and i not in visited:
            dfs(i,visited)
    return visited

print(len(dfs(1,[]))-1)