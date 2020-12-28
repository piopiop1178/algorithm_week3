import sys
from collections import deque
sys.stdin = open("input.txt", "r")
go=sys.stdin.readline

m,n,h=map(int,go().split())
zone=[[list(map(int, list(go().split()))) for _ in range(n)] for _ in range(h)]
#print(zone)

dx=[-1,1,0,0,0,0]
dy=[0,0,-1,1,0,0]
dz=[0,0,0,0,-1,1]
visited=deque()
for i in range(n):
    for j in range(m):
        for k in range(h):
            if zone[k][i][j] == 1:
                visited.append([i,j,k])

def bfs():
    while visited:
        a, b, c = visited.popleft()
        for i in range(6):
            x = a+dx[i]
            y = b+dy[i]
            z = c+dz[i]
            if 0<=x<n and 0<=y<m and 0<=z<h:
                if zone[z][x][y]==0:
                    visited.append([x,y,z])
                    zone[z][x][y]=zone[c][a][b]+1

bfs()

z=1
result=-1

for i in zone:
    for j in i:
        for k in j:
            if k ==0:
                z = 0
            result=max(result,k)

if z ==0:
    print(-1)
elif result ==1:
    print(0)
else:
    print(result-1)
