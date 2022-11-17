"""
이것이 취업을 위한 코딩 테스트다 with 파이썬, 한빛 미디어, 나동빈
p. 321
기출 7. 럭키 스트레이트
"""
n = input()
length = len(n)
left = sum(list(map(int, n[:length//2])))
right = sum(list(map(int, n[length//2:])))
print("LUCKY" if left == right else "READY")
