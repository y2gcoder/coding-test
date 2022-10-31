'''
이것이 취업을 위한 코딩 테스트다 with 파이썬, 한빛 미디어, 나동빈
P.87
예제 3-1
'''

n = int(input())
c = (500, 100, 50, 10)

result = 0

for i in c:
    while n >= i:
        n = n - i
        result += 1


print(result)