"""
이것이 취업을 위한 코딩 테스트다 with 파이썬, 한빛 미디어, 나동빈
p. 149
실전 문제 3. 음료수 얼려먹기
"""

n, m = map(int, input().split())


def dfs(x, y):
    # 얼음 넣기
    if x < 0 or x >= n or y < 0 or y >= m:
        return False

    if graph[x][y] == 1:
        return False

    graph[x][y] = 1
    dfs(x - 1, y)
    dfs(x + 1, y)
    dfs(x, y - 1)
    dfs(x, y + 1)
    return True


graph = []
for i in range(n):
    graph.append(list(map(int, input())))


result = 0


for i in range(n):
    for j in range(m):
        if dfs(i, j):
            result += 1

print(result)

