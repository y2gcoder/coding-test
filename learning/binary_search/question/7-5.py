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


n = int(input())
array_n = list(map(int, input().split()))
m = int(input())
array_m = list(map(int, input().split()))

array_n.sort()
array_m.sort()


for target in array_m:
    message = "no"
    if binary_search(array_n, target, 0, n - 1) == True:
        message = "yes"
    print(message, end=' ')
