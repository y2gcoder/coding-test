"""
이것이 취업을 위한 코딩 테스트다 with 파이썬, 한빛 미디어, 나동빈
p. 311
기출 문제 1. 모험가 길드
"""

n = int(input())
data = list(map(int, input().split()))

data.sort(reverse=True)

count = 0
while True:
    if len(data) <= 0:
        break
    group_count = data[0]
    if len(data) >= group_count:
        count += 1
        del data[:group_count]
    else:
        break

print(count)


