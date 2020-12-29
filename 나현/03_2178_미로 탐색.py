import sys
sys.stdin = open("input.txt", "r")
input=sys.stdin.readline

n, m = map(int,input().split())
zone=[]
for _ in range(n):
    line=list(input())
    zone.append(line)
# zone=[list(map(int, list(input()))) for _ in range(n)]
# 위 쓸때는 input=sys.stdin.readline 적용X
# 아니면 그냥 아래 쓸것!
# zone=[list(map(int, list(sys.stdin.readline().rstrip()))) for _ in range(n)]

# check=[[False]*m for _ in range(n)]
# check[0][0]=True
zone[0][0]=1
visited=[[0,0]]
dx=[-1,1,0,0]
dy=[0,0,-1,1]

while visited:
    a, b = visited[0][0], visited[0][1]
    visited.pop(0)
    for i in range(4):
        x = a+dx[i]
        y = b+dy[i]
        if 0<=x<n and 0<=y<m and zone[x][y]=='1':
            # and check[x][y] == False
            visited.append([x,y])
            zone[x][y]=zone[a][b]+1
            # check[x][y]=True
print(zone[n-1][m-1])

'''
if x + 1 < N and visited[x+1][y] == 0 and matrix[x+1][y] == '1':
    visited[x+1][y] = visited[x][y] + 1
    queue.append((x+1, y))
if 0 <= x - 1  and visited[x-1][y] == 0 and matrix[x-1][y] == '1':
    visited[x-1][y] = visited[x][y] + 1
    queue.append((x-1, y))
if y + 1 < M and visited[x][y + 1] == 0 and matrix[x][y + 1] == '1':
    visited[x][y + 1] = visited[x][y] + 1
    queue.append((x, y + 1))
if 0 <= y - 1 and visited[x][y - 1] == 0 and matrix[x][y - 1] == '1':
    visited[x][y - 1] = visited[x][y] + 1
    queue.append((x, y - 1))
'''