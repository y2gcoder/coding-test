n, m = map(int, input().split())
graph = []

for i in range(n):
    graph.append(list(map(int, input().split())))


def get_chicken_distance(x, y):
    result = int(1e9)
    for i in range(n):
        for j in range(n):
            if graph[i][j] == 2:
                value = abs(x - i) + abs(y - j)
                result = min(result, value)
    return result


distances = []
for i in range(n):
    for j in range(n):
        if graph[i][j] == 1:
            distances.append(get_chicken_distance(i, j))

distances.sort()

print(sum(distances[0:0+m]))
