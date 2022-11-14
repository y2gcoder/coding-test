"""
이것이 취업을 위한 코딩 테스트다 with 파이썬, 한빛 미디어, 나동빈
p. 315
기출 문제 5. 볼링 공 고르기
"""
from itertools import combinations

n, m = map(int, input().split())
data = list(map(int, input().split()))

count = 0

"""
조합으로 값을 구하고, 뺄까?
"""

comb = list(combinations(data, 2))

for x in comb:
    if x[0] != x[1]:
        count += 1


print(count)
