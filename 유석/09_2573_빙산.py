import sys
sys.stdin = open("../../../test/glacier.txt", "r")
read = sys.stdin.readline
M, N = map(int, read().rstrip().split())
stack = []
ocean = [list(map(int, read().rstrip().split())) for _ in range(M)]
dx = (1, 0, -1, 0)
dy = (0, 1, 0, -1)
temp_dic = {}


def melt(x, y):
    result = ocean[x][y]
    for i in range(4):
        temp_x = x + dx[i]
        temp_y = y + dy[i]
        if 0 <= temp_x < M and 0 <= temp_y < N:
            if not ocean[temp_x][temp_y]:
                result -= 1
    if result <= 0:
        return 0
    else:
        return result


def dfs():
    answer = 0
    while True:
        glacier = 0
        for x in range(M):
            for y in range(N):
                if ocean[x][y] and (x, y) not in temp_dic: # 새로운게 나오자마자 리턴하니까 문제가 발생했다...
                    glacier += 1
                    if glacier >= 2:
                        print(x, y)
                        return answer
                    stack.append((x, y))
                    temp_dic[(x, y)] = melt(x, y)
                    while stack:
                        # print(stack)
                        # print(temp_dic)
                        x, y = stack.pop()
                        for i in range(4):
                            temp_x = x + dx[i]
                            temp_y = y + dy[i]
                            if 0 <= temp_x < M and 0 <= temp_y < N:
                                if ocean[temp_x][temp_y] and (temp_x, temp_y) not in temp_dic:
                                    temp_dic[(temp_x, temp_y)] = melt(temp_x, temp_y)
                                    stack.append((temp_x, temp_y))
        print(temp_dic)
        if not temp_dic:
            return 0
        for key, value in temp_dic.items():
            x, y = key
            ocean[x][y] = value
        temp_dic.clear()
        answer += 1
        print(glacier)
        for i in range(M):
            print(*ocean[i])
        print()


print(dfs())