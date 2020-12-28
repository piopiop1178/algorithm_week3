import sys
sys.stdin = open("../../../test/glacier.txt", "r")
read = sys.stdin.readline
M, N = map(int, read().rstrip().split())
stack = []
check_list = []
glacier = [list(map(int, read().rstrip().split())) for _ in range(M)]
dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

def check(x, y):
    count = 0
    for i in range(len(dx)):
        around_x, around_y = x+dx[i], y+dy[i]
        if 0 <= around_x < M and 0 <= around_y < N:
            if not glacier[around_x][around_y]:
                count += 1
    if glacier[x][y] <= count:
        return 0
    else:
        return glacier[x][y] - count

g_count = 0
count = 0
while g_count < 2:
    count += 1
    for x in range(M):
        for y in range(N):
            if not glacier[x][y] and (x, y) not in check_list:
                g_count += 1
                stack.append((x, y))
                check_list.append((x, y))
                while True:
                    for i in range(len(dx)):
                        next_x, next_y = x+dx[i], y+dy[i]
                        if 0 <= next_x < M and 0 <= next_y < N:
                            if not glacier[next_x][next_y] and (next_x, next_y) not in check_list:
                                stack.append((next_x, next_y))
                                check_list.append((next_x, next_y))
                                x, y = next_x, next_y
            while stack:
                now_x, now_y = stack.pop()
                glacier[now_x][now_y] = check(now_x, now_y)

print(count)