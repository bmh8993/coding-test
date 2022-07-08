# 입력 예시
# 4 5   <- 얼음 틀의 세로길이 N, 가로길이 M
# 00110
# 00011
# 11111
# 00000

n, m = map(int, input().split())

graph = []
for i in range(n):
    graph.append(list(map(int, input())))

result = 0
for i in range(n):
    for j in range(m):
        if dfs(i, j) == True:
            result += 1
print(result)


def dfs(x, y):

    if x <= -1 or x >= n or y <= -1 or y >= m:
        return False

    # 방문하지 않은 경우 방문처리
    if graph[x][y] == 0:
        graph[x][y] == 1

        dfs(x - 1, y)
        dfs(x + 1, y)
        dfs(x, y - 1)
        dfs(x, y + 1)

        return True
    return False

