"""
이것이 취업을 위한 코딩 테스트다 with 파이썬, 한빛 미디어, 나동빈
p. 313
기출 문제 3. 문자열 뒤집기
"""

data = input()

count = 0
first = int(data[0])    # 처음 숫자
previous = int(data[0])  # 직전 숫자
for i in range(1, len(data)):
    num = int(data[i])
    if previous == num: # 직전 숫자와 같으면 건너뛰기
        continue
    else:   # 직전 숫자와 같지 않다면
        if first != num:    #   처음 숫자와 같지 않다면
            count += 1  # 숫자를 뒤집어준다.
        previous = num  # 직전 숫자 갱신


print(count)
