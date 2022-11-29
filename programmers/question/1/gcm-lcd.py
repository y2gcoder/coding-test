"""
프로그래머스
코딩테스트 연습
최대공약수와 최소공배수
https://school.programmers.co.kr/learn/courses/30/lessons/12940
"""


"""
유클리드 호제법 이용
GCD(A, B) = GCD(B, A % B)
if A % B = 0 -> GCD = B
else GCD(B, A % B)
"""
def gcd(a, b):
    if a % b == 0:
        return b
    return gcd(b, a % b)


def solution(n, m):
    return [gcd(n, m), (n * m) // gcd(n, m)]




