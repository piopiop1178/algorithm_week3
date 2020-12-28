import sys
from collections import deque
sys.stdin = open("../../../test/escape.txt", "r")
R, C = map(int, sys.stdin.readline().split())
forest = list()
for _ in range(R):
    forest.append(list(sys.stdin.readline().rstrip()))

water = deque()
hedgehog = deque()

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]


def bfs():
    time = 0
    for i in range(R):
        for j in range(C):
            if forest[i][j] == "*":
                water.append((i, j))
            if forest[i][j] == "S":
                hedgehog.append((i, j))
    hedgehog.append(1)
    water.append(1)
    while hedgehog:
        while water:
            if water[0] != 1:
                w_x, w_y = water.popleft()
                for i in range(4):
                    n_w_x, n_w_y = w_x + dx[i], w_y + dy[i]
                    if 0 <= n_w_x < R and 0 <= n_w_y < C:
                        next_water = forest[n_w_x][n_w_y]
                        if next_water != "D" and next_water != "X" and next_water != "*":
                            forest[n_w_x][n_w_y] = "*"
                            water.append((n_w_x, n_w_y))
            else:
                water.popleft()
                water.append(1)
                break
        while hedgehog[0] != 1:
            h_x, h_y = hedgehog.popleft()
            for i in range(4):
                n_h_x, n_h_y = h_x + dx[i], h_y + dy[i]
                if 0 <= n_h_x < R and 0 <= n_h_y < C:
                    next_hedgehog = forest[n_h_x][n_h_y]
                    if next_hedgehog == ".":
                        forest[n_h_x][n_h_y] = "S"
                        hedgehog.append((n_h_x, n_h_y))
                    if next_hedgehog == "D":
                        return time+1
        if len(hedgehog) != 1:
            time += hedgehog.popleft()
            hedgehog.append(1)
        else:
            return "KAKTUS"


print(bfs())