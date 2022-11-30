"""
이것이 취업을 위한 코딩 테스트다 with 파이썬, 한빛 미디어, 나동빈
p. 180
실전 3. 성적이 낮은 순서로 학생 출력하기
"""

n = int(input())

grades = []
for i in range(n):
    data = input().split()
    grades.append((data[0], int(data[1])))

result = sorted(grades, key=lambda x: x[1])

for i in result:
    print(i[0], end=' ')
