n = int(input())
x = list(map(int, input().split()))

x.sort()

result = 0
i = 0
while i < n:
    member = x[i]
    result += 1
    i += x[i]

print(result)
