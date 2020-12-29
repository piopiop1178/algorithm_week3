import sys
sys.stdin = open("input.txt", "r")
#input=sys.stdin.readline

n, m = map(int, input().split())
zone=[list(map(int, list(sys.stdin.readline().split()))) for _ in range(n)]
cnt=0
ans=0
dx=[-1,1,0,0]
dy=[0,0,-1,1]
ice=[]
for i in range(n):
    for j in range(m):
        if zone[i][j]!=0:
            ice.append([i,j])

def concheck(y,x):
    global n,m
    visited=[[False]*m for _ in range(n)]
    visited[y][x]=True
    c = []
    c.append([y,x])
    con=1
    while c:
        y, x=c.pop()
        for i in range(4):
            ny=y+dy[i]
            nx=x+dx[i]
            if not visited[ny][nx] and zone[ny][nx]!=0:
                c.append([ny,nx])
                visited[ny][nx]=True
                con+=1
    return con

melt= [[0] * m for _ in range(n)]
while ice:
    if len(ice) != concheck(ice[0][0],ice[0][1]):
        ans=cnt
        break
    me=[]
    cnt+=1
    for i in range(len(ice)-1, -1, -1):
        y,x=ice[i]
        for j in range(4):
            ny=y+dy[j]
            nx=x+dx[j]
            if zone[ny][nx]==0:
                melt[y][x]+=1
        if melt[y][x]>0:
            me.append([y,x,i])
    for y, x, i in me:
        zone[y][x]-=melt[y][x]
        if zone[y][x]<=0:
            zone[y][x]=0
            ice.pop(i)
        melt[y][x]=0

print(ans)
