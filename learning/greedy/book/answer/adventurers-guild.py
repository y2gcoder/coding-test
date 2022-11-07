"""
이것이 취업을 위한 코딩 테스트다 with 파이썬, 한빛 미디어, 나동빈
p. 506
기출 문제 1. 모험가 길드
"""

n = int(input())
data = list(map(int, input().split()))
data.sort()

result = 0  # 총 그룹 수
count = 0   # 현재 그룹에 포함된 모험가의 수

for i in data:  # 공포도가 낮은 것부터 하나씩 확인하며
    count += 1  # 현재 그룹에 해당 모험가를 포함시키기
    if count >= i:  # 현재 그룹에 포함된 모험가의 수가 현재의 공포도 이상이라면, 그룹 결성
        result += 1 # 총 그룹의 수 증가시키기
        count = 0   # 현재 그룹에 포함된 모험가 수 초기화

print(result)   # 총 그룹 수 출력


