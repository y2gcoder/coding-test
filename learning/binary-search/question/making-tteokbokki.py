"""
이것이 취업을 위한 코딩 테스트다 with 파이썬, 한빛 미디어, 나동빈
p. 201
실전 문제 3. 떡볶이 떡 만들기
"""

n, m = map(int, input().split())
data = list(map(int, input().split()))


def binary_search(array, target):
    start = 0
    end = max(array)
    result = []
    while start <= end:
        mid = (start + end) // 2
        cut = list(map(lambda x: x-mid if x-mid >= 0 else 0, array))
        if sum(cut) > target:
            start = mid + 1
        elif sum(cut) < target:
            end = mid - 1
        else:
            return mid


    return max(result)


print(binary_search(data, m))
