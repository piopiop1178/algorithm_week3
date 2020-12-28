import sys
from collections import deque
sys.stdin = open("input.txt", "r")

N, M = map(int, sys.stdin.readline().split())
m = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]

def solution(m):
    land = []
    for x in range(1, M - 1):
        for y in range(1, N - 1):
            if m[y][x] > 0:
                land.append((x, y))
    
    dxy = [(1, 0), (-1, 0), (0, 1), (0, -1)]
    cnt = 0
    answer = 1

    while True:
        check_1 = [[0] * M for _ in range(N)]
        new_land = []
        for x, y in land:
            if m[y][x] > 0:
                sea_cnt = 0
                for d in dxy:
                    nx, ny = x + d[0], y + d[1]
                    if not check_1[ny][nx] and m[ny][nx] <= 0:
                        sea_cnt += 1
                m[y][x] -= sea_cnt
                check_1[y][x] = 1
                if m[y][x] > 0:
                    new_land.append((x, y))
        land = new_land
        
        check_2 = [[0] * M for _ in range(N)]
        for x, y in land:
            if m[y][x] > 0 and not check_2[y][x]:
                queue = deque([(x, y)])
                check_2[y][x] = 1
                while queue:
                    tx, ty = queue.popleft()
                    for d in dxy:
                        nx, ny = tx + d[0], ty + d[1]
                        if m[ny][nx] > 0 and not check_2[ny][nx]:
                            queue.append((nx, ny))
                            check_2[ny][nx] = 1
                cnt += 1
                if cnt >= 2:
                    return answer
        if cnt == 0:
            return 0        
        answer += 1
        cnt = 0
print(solution(m))