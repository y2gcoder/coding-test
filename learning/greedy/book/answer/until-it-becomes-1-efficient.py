"""
이것이 취업을 위한 코딩 테스트다 with 파이썬, 한빛 미디어, 나동빈
p. 102
실전 문제 4. 1이 될 때까지 (효율)
"""

# N, K를 공백으로 구분하여 입력받기
n, k = map(int, input().split())
result = 0


while True:
    # (N == K로 나누어떨어지는 수)가 될 때까지 1씩 빼기
    target = (n // k) * k
    result += (n - target)
    n = target
    # N이 K보다 작을 때(더 이상 나눌 수 없을 때) 반복문 탈출
    if n < k:
        break
    # K로 나누기
    result += 1
    n //= k

# 마지막으로 남은 수에 대하여 1씩 빼기
result += (n - 1)   # 0이 되었을 때 하나 돌려줌. 위의 1씩 빼기 해서 0이 될 때 보상이 됨!
print(result)
