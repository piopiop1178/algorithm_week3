import sys
sys.stdin = open("input.txt", "r")
input=sys.stdin.readline

r, c = map(int, input().split())
zone=[list(map(lambda x:ord(x)-65, input())) for i in range(r)]
dx=[-1,1,0,0]
dy=[0,0,-1,1]
cnt = 1
visited=[0]*26

def dfs(a, b, tmp):
    global cnt, visited
    cnt = max(cnt, tmp)

    for i in range(4):
        x = a+dx[i]
        y = b+dy[i]
        if 0<=x<r and 0<=y<c and visited[zone[x][y]]==0:
            visited[zone[x][y]]=1
            dfs(x, y, tmp+1)
            visited[zone[x][y]]=0

visited[zone[0][0]] = 1
dfs(0,0,1)
print(cnt)

'''
r, c = map(int, input().split())
zone=[list(map(str, list(input().rstrip()))) for _ in range(r)]
dx=[-1,1,0,0]
dy=[0,0,-1,1]
cnt = 1
visited=[zone[0][0]]

def dfs(a, b, tmp):
    global cnt, visited
    cnt = max(cnt, tmp)

    for i in range(4):
        x = a+dx[i]
        y = b+dy[i]
        if 0<=x<r and 0<=y<c and zone[x][y] not in visited:
            visited.append(zone[x][y])
            dfs(x, y, tmp+1)
            visited.remove(zone[x][y])

dfs(0,0,1)
print(cnt)
'''

'''
def bfs(x,y):
    global cnt
    q = set([(x,y,zone[x][y])])
    while q:
        x, y, tmp = q.pop()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < r and 0 <= ny < c and (zone[nx][ny] not in tmp):
                q.add((nx,ny,tmp+zone[nx][ny]))
                cnt = max(cnt, len(tmp)+1)

bfs(0,0)
print(cnt)
'''