"""
이것이 취업을 위한 코딩 테스트다 with 파이썬, 한빛 미디어, 나동빈
p. 197
실전 문제 2. 부품 찾기
"""

n = int(input())
parts = list(map(int, input().split()))

m = int(input())
requests = list(map(int, input().split()))

parts.sort()


def binary_search(array, target, start, end):
    if start > end:
        return False
    mid = (start + end) // 2
    if array[mid] == target:
        return True
    elif array[mid] > target:
        return binary_search(array, target, start, mid - 1)
    else:
        return binary_search(array, target, mid + 1, end)


for r in requests:
    if binary_search(parts, r, 0, n - 1):
        print("yes", end=" ")
    else:
        print("no", end=" ")