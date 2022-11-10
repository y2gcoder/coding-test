"""
이것이 취업을 위한 코딩 테스트다 with 파이썬, 한빛 미디어, 나동빈
p. 113
예제 4-2. 시각
"""

n = int(input())

count = 0

for h in range(n + 1):
    sh = str(h)
    for m in range(60):
        sm = str(m)
        for s in range(60):
            ss = str(s)
            data = sh + sm + ss
            if '3' in data:
                count += 1

print(count)
