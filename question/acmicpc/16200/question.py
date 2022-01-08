n = int(input())
x = list(map(int, input().split()))

count = [0] * (max(x) + 1)

for i in range(len(x)):
    count[x[i]] += 1

result = 0
for i in range(len(count)):
    if i == 0:
        continue
    result += count[i] // i
    if count[i] % i != 0:
        if i >= len(count) - 1:
            result += 1
        else:
            count[i+1] += 1

print(result)
