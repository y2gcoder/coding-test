n = int(input())
data = list(map(int, input().split()))

data.sort()

result = 0
team = 0

for i in range(n):
    team += 1
    if team == data[i]:
        result += 1
        team = 0


print(result)
