import sys
# sys.stdin = open("../../../test/alphabet.txt", "r")
R, C = map(int, sys.stdin.readline().split())
read = sys.stdin.readline
board = list()
for _ in range(R):
    board.append(list(map(lambda x: ord(x)-65, list(read().rstrip()))))
check = list(0 for _ in range(26))

answer = 0
def dfs(x, y, count):
    global answer
    check[board[x][y]] = 1
    count += 1
    answer = max(count, answer)
    if x - 1 >= 0 and not check[board[x-1][y]]:
        dfs(x-1, y, count)
    if x + 1 < R and not check[board[x+1][y]]:
        dfs(x+1, y, count)
    if y - 1 >= 0 and not check[board[x][y-1]]:
        dfs(x, y-1, count)
    if y + 1 < C and not check[board[x][y+1]]:
        dfs(x, y+1, count)
    check[board[x][y]] = 0

dfs(0, 0, 0)
print(answer)