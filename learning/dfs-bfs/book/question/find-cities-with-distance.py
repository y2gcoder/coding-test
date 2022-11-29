"""
이것이 취업을 위한 코딩 테스트다 with 파이썬, 한빛 미디어, 나동빈
p. 339
기출 문제 15. 특정 거리의 도시 찾기
"""

from collections import deque

n, m, k, x = map(int, input().split())

# bfs, distances 하자

graph = [[] for _ in range(n + 1)]

for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)


distances = [-1] * (n + 1)
distances[x] = 0

q = deque([x])

while q:
    now = q.popleft()
    for next_node in graph[now]:
        if distances[next_node] == -1:
            distances[next_node] = distances[now] + 1
            q.append(next_node)

if distances.count(k) < 1:
    print(-1)
else:
    for i in range(1, n + 1):
        if distances[i] == k:
            print(i)
