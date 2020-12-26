import sys
sys.stdin = open("../../../test/alphabet.txt", "r")
R, C = map(int, sys.stdin.readline().split())
read = sys.stdin.readline
board = list()

for _ in range(R):
    board.append(list(map(lambda x: ord(x)-65, list(read().rstrip()))))

check = list(0 for _ in range(26))

def dfs(x, y, count):
    if 0 <= x < R and 0 <= y < C:
        if check[board[x][y]] == 0:
            check[board[x][y]] = 1
            count += 1
            count = max(dfs(x-1, y, count),
                        dfs(x+1, y, count),
                        dfs(x, y-1, count),
                        dfs(x, y+1, count))
            check[board[x][y]] = 0
    return count


print(dfs(0, 0, 0))