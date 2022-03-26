s = list(map(int, input()))
print(s)
result = 0
initialNumber = s[0]
prevNumber = s[0]

for i in range(1, len(s)):
    if s[i] != prevNumber and s[i] != initialNumber:
        result += 1
    prevNumber = s[i]

print(result)
