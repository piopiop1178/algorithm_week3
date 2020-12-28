import sys
sys.stdin = open("input.txt", "r")
input=sys.stdin.readline

n, k = map(int, input().split())
coin=[]
for _ in range(n):
    coin.append(int(input()))
cnt=[0]*(k+1)

def solve():
    for i in range(1,k+1):
        a=[]
        for j in coin:
            if j<=i and cnt[i-j] != -1:
                a.append(cnt[i-j])
        if not a:
            cnt[i]=-1
        else:
            cnt[i]=min(a)+1
        print(cnt[i])
    return cnt[k]

print(solve())

'''
cnt=[10001]*(k+1)
cnt[0]=0

for i in range(n):
    for j in range(coin[i], k+1):
        cnt[j] = min(cnt[j], cnt[j-coin[i]] + 1)

cnt[-1] = cnt[-1] if cnt[-1] != 10001 else -1
print(cnt[-1])
'''

'''
def bfs():
    while q:
        t, cnt = q.popleft()
        cnt+=1
        for coin in coins:
            nt = t+coin
            if nt<k:
                if d[nt]>cnt:
                    q.append([nt,cnt])
                    d[nt] = cnt
            elif nt==k:
                return cnt
    return -1
    
d=[10001]*(k+1)
for c in coins:
    if c <=k:
        d[c]=1
        q.append([c,1])
if d[k] ==1:
    print(1)
else:
    print(bfs())
'''