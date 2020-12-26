import sys
sys.stdin = open("input.txt", "r")  

R, C = map(int, sys.stdin.readline().split())
board = [list(map(lambda x:ord(x) - 65, sys.stdin.readline().rstrip())) for _ in range(R)]
dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]
check = [False] * 26
answer = 1

def dfs(x, y, n):
    global answer
    n += 1
    answer = max(answer, n)
    
    check[board[y][x]] = True
    for i in range(4):
        nx, ny = x + dx[i], y + dy[i]
        if 0 <= nx < C and 0 <= ny < R:
            if not check[board[ny][nx]] :
                dfs(nx, ny, n)
    check[board[y][x]] = False

dfs(0, 0, 0)
print(answer)
#왜 set이 더 느린지???? 
#메모이제이션