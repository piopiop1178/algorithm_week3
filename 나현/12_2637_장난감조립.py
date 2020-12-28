import sys
from collections import deque
sys.stdin = open("input.txt", "r")
input=sys.stdin.readline

n= int(input())
m= int(input())
toy = [[]for _ in range(n+1)]
indegree = [0 for _ in range(n+1)]
q =deque()
a=[[0]*(n+1) for _ in range(n+1)]

for _ in range(m):
    i, j, k = map(int, input().split())
    toy[i].append([j,k])
    indegree[j] +=1

for i in range(1, n+1):
    if indegree[i] ==0:
        q.append(i)
        a[i][i]=1

while q:
    i = q.popleft()
    for j in student[i]:
        indegree[j] -=1
        a[i][j] += a
        if indegree[j] == 0:
            q.append(j)
    print(i, end=' ')
