import sys
from collections import deque
sys.stdin = open("../../../test/maze.txt", "r")
N, M = map(int, sys.stdin.readline().split())
maze = list()
for _ in range(N):
    maze.append(list(map(int, sys.stdin.readline().rstrip())))

dq = deque()


def bfs(start_x, start_y, count):
    dq.append((start_x, start_y, count))
    while dq:
        x, y, count = dq.popleft()
        if 0 <= x < N and 0 <= y < M:
            if maze[x][y] == 1:
                count += 1
                if (x, y) == (N-1, M-1):
                    break
                maze[x][y] = 0
                dq.append((x+1, y, count))
                dq.append((x, y+1, count))
                dq.append((x-1, y, count))
                dq.append((x, y-1, count))
    return count


print(bfs(0, 0, 0))
