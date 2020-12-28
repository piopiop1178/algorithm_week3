import sys
sys.stdin = open("input.txt", "r")
N = int(sys.stdin.readline())
M = int(sys.stdin.readline())
arr = [[] for _ in range(N + 1)]
cnt = [0] * (N + 1)
answer = [0] * (N + 1)
answer[N] = 1

for _ in range(M):
    X, Y, K = map(int, sys.stdin.readline().split())
    arr[X].append([Y, K])
    cnt[Y] += 1

queue = [N]
while queue:
    target = queue.pop()
    for n, m in arr[target]:
        answer[n] += m * answer[target]
        cnt[n] -= 1
        if cnt[n] == 0:
            queue.append(n)

for i in range(1, N + 1):
    if not arr[i] and answer[i] != 0:
        print(i, answer[i])    
