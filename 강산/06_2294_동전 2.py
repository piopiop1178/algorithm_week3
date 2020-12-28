import sys
from collections import deque
n, k = map(int, sys.stdin.readline().split())
coins = set()
queue = deque([])
dp = [0] * (k + 1)

for _ in range(n):
    coin = int(sys.stdin.readline())
    if coin <= k:
        coins.add(coin)
        queue.append((coin, 1))
        dp[coin] = 1

def bfs(queue, dp, k):
    while queue:
        v, n = queue.popleft()
        for c in coins:
            new_v = v + c
            if new_v <= k:
                if new_v == k:
                    return n + 1
                if not dp[new_v] or dp[new_v] > n + 1:
                    dp[new_v] = n + 1
                    queue.append((new_v, n +1 ))
    return -1 if dp[k] == 0 else dp[k]

print(bfs(queue, dp, k))