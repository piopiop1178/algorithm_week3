import sys
sys.stdin = open("input.txt", "r")
input=sys.stdin.readline

n= int(input())
m= int(input())
toy = [[]for _ in range(n+1)]
indegree = [0 for _ in range(n+1)]
ans=[0 for _ in range(n+1)]
ans[n]=1

for _ in range(m):
    i, j, k = map(int, input().split())
    toy[i].append([j,k])
    indegree[j] +=1

q=[n]
while q:
    i = q.pop()
    for j, k in toy[i]:
        indegree[j] -=1
        ans[j] += k * ans[i]
        if indegree[j] == 0:
            q.append(j)

for i in range(1, n+1):
    if not toy[i] and ans[i] != 0:
        print(i, ans[i])
