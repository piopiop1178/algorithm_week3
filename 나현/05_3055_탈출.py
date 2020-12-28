import sys
from collections import deque
sys.stdin = open("input.txt", "r")
input=sys.stdin.readline

r, c = map(int, input().split())
zone=[]
visited=[[0]*c for _ in range(r)]
w=deque()
q=deque()

dx=[-1,1,0,0]
dy=[0,0,-1,1]

def bfs():
    while q or w:
        tmp1=[]
        tmp2=[]
        while q:
            a, b = q.popleft()
            if zone[a][b] != '*':
                for i in range(4):
                    x = a+dx[i]
                    y = b+dy[i]
                    if 0<=x<r and 0<=y<c and zone[x][y]!='*' and zone[x][y]!='X' and visited[x][y]==0:
                        visited[x][y]=1
                        zone[x][y]=zone[a][b]+1
                        tmp1.append([x,y])
        while w:
            a, b = w.popleft()
            for i in range(4):
                x = a + dx[i]
                y = b + dy[i]
                if x == d[0] and y==d[1]:
                    continue
                if 0 <= x < r and 0 <= y < c and zone[x][y] != '*' and zone[x][y] != 'X':
                    zone[x][y] = '*'
                    tmp2.append([x, y])

        for i in tmp1:
            q.append(i)
        for i in tmp2:
            w.append(i)

for i in range(r):
    a = list(input().strip())
    zone.append(a)
    for j in range(c):
        if a[j]=='D':
            d = [i,j]
        elif a[j]=='S':
            q.append([i,j])
            visited[i][j]=1
            zone[i][j]=0
        elif a[j]=='*':
            w.append([i,j])

bfs()
result=zone[d[0]][d[1]]
print(result if result!='D' else 'KAKTUS')
