n, m, k = map(int, input().split())
data = list(map(int, input().split()))

data.sort(reverse=True)

one = data[0]
two = data[1]

result = 0

while True:
    for i in range(k):
        if m == 0:
            break
        result += one
        m -= 1
    if m == 0:
        break
    result += two
    m -= 1

print(result)



