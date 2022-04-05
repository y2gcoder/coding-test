from bisect import bisect_left, bisect_right

n, x = map(int, input().split())
data = list(map(int, input().split()))

right_index = bisect_right(data, x)
left_index = bisect_left(data, x)

if right_index - left_index == 0:
    print(-1)
else:
    print(right_index - left_index)
