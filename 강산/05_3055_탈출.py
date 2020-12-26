import sys
from collections import deque

sys.stdin = open("input.txt", "r")
R, C = map(int, sys.stdin.readline().split())
m = [list(sys.stdin.readline().rstrip()) for _ in range(R)]

def bfs(m):
    dxy = [(1, 0), (-1, 0), (0, 1), (0, -1)]
    queue = deque([])
    water_queue = deque([])
    check = [[0] * C for _ in range(R)]

    for y in range(R):
        for x in range(C):
            if m[y][x] == '*':
                water_queue.append((x, y, 0))
            if m[y][x] == 'S':
                queue.append((x, y, 0))
                check[y][x] = 1

    while water_queue:
        x, y, t = water_queue.popleft()
        for d in dxy:
            nx, ny = x + d[0], y + d[1]
            if 0 <= nx < C and 0 <= ny < R:
                if m[ny][nx] == '.':
                    m[ny][nx] = t + 1
                    water_queue.append((nx, ny, t + 1))
                    
    for y in range(R):
        for x in range(C):
            if m[y][x] == '.':
                m[y][x] = float('inf')

    while queue:
        x, y, t = queue.popleft()
        for d in dxy:
            nx, ny = x + d[0], y + d[1]
            if 0 <= nx < C and 0 <= ny < R:
                if m[ny][nx] != 'S' and m[ny][nx] != 'X' and m[ny][nx] != '*':
                    if m[ny][nx] == 'D':
                        return t + 1
                    else:
                        if m[ny][nx] > t + 1 and not check[ny][nx]:
                            queue.append((nx, ny, t + 1))
                            check[ny][nx] = 1
    return 'KAKTUS'

print(bfs(m))
                    
