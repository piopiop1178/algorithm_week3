import sys
from collections import deque
sys.stdin = open("input.txt", "r")
input=sys.stdin.readline

n, m = map(int, input().split())
student = [[]for _ in range(n+1)]
indegree = [0 for _ in range(n+1)]
q =deque()

for _ in range(m):
    i, j = map(int, input().split())
    student[i].append(j)
    indegree[j] +=1

for i in range(1, n+1):
    if indegree[i] ==0:
        q.append(i)

while q:
    i = q.popleft()
    for j in student[i]:
        indegree[j] -=1
        if indegree[j] == 0:
            q.append(j)
    print(i, end=' ')
