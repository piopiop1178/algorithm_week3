import sys
from collections import deque
sys.stdin = open("input.txt", "r")
input=sys.stdin.readline

'''
n, m=map(int, input().split())
heavy=[[] for _ in range(n+1)]
light=[[] for _ in range(n+1)]
mid=n//2
ans=0

def hbfs(v):
    global ans
    q=deque()
    visited=[False]*(n+1)
    visited[v]=True
    q.append(v)
    cnt=0

    while q:
        v=q.popleft()
        for i in heavy[v]:
            if not visited[i]:
                visited[i]=True
                cnt+=1
                if cnt>mid:
                    ans +=1
                    return
                q.append(i)

def lbfs(v):
    global ans
    q = deque()
    visited = [False] * (n + 1)
    visited[v] = True
    q.append(v)
    cnt = 0

    while q:
        v = q.popleft()
        for i in light[v]:
            if not visited[i]:
                visited[i] = True
                cnt += 1
                if cnt > mid:
                    ans += 1
                    return
                q.append(i)

for _ in range(m):
    a, b=map(int, input().split())
    heavy[b].append(a)
    light[a].append(b)

for i in range(1, n+1):
    hbfs(i)
    lbfs(i)

print(ans)
'''

def find(dataset, start):
    global visited
    global check
    visited[start] = True
    for val in dataset[start]:
        if not visited[val]:
            check+=1
            find(dataset, val)

N, M=map(int, input().split())
datas=list(tuple(map(int, input().split()))for i in range(M))

mid=(N+1)//2
more = [[] for i in range(N + 1)]
less = [[] for i in range(N + 1)]
for (a, b) in datas:
    more[b].append(a)
    less[a].append(b)

count = 0
check = 0
visited = None
for i in range(1, N + 1):
    visited = [False for i in range(N + 1)]

    check = 0
    find(more, i)
    if (check >= mid):
        count += 1

    check = 0
    find(less, i)
    if (check >= mid):
        count += 1
print(count)
