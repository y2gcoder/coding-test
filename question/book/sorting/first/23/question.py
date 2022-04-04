n = int(input())
data = []
for i in range(n):
    name, a, b, c = input().split()
    data.append((int(a), int(b), int(c), name))

data.sort(key=lambda x: (-x[0], x[1], -x[2], x[3]))

for i in range(n):
    print(data[i][3])
