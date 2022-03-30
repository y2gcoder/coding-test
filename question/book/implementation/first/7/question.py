n = list(map(int, input()))

half = int(len(n) / 2 - 1)

left = 0
right = 0

for i in range(half + 1):
    left += n[i]

for i in range(half + 1, len(n)):
    right += n[i]

if left == right:
    print("LUCKY")
else:
    print("READY")
